import json
import time
import resource

def lambda_handler(event, context):
    try:
        # Get the code, multiple input sets, and expected outputs from the event
        code = event.get('code')
        input_sets = event.get('input_sets', [])
        expected_outputs = event.get('expected_outputs', [])

        # Prepare to store results
        results = []

        total_execution_time = 0
        total_memory_used = 0
        num_inputs = len(input_sets)

        # Iterate through each set of inputs and execute the code
        for idx, inputs in enumerate(input_sets):
            local_vars = {}

            # Start timing
            start_time = time.time()

            # Get initial memory usage
            initial_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            
            # Execute the code snippet
            exec(code, {}, local_vars)

            # Check if 'Solution' function exists in the user's code
            if 'Solution' in local_vars:
                result = local_vars['Solution'](**inputs)
            else:
                result = "No 'Solution' function defined in the provided code."

            # End timing
            end_time = time.time()

            # Get final memory usage
            final_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

            # Calculate execution time and memory usage for this input set
            execution_time = end_time - start_time  # in seconds
            memory_used = final_memory - initial_memory  # in kilobytes

            # Add to total execution time and memory used
            total_execution_time += execution_time
            total_memory_used += memory_used

            expected_output = expected_outputs[idx] if idx < len(expected_outputs) else None
            results.append({
                'input_set': inputs,
                'actual_output': result,
                'expected_output': expected_output,
                'is_match': result == expected_output if expected_output is not None else None,
                'execution_time': execution_time,  # in seconds
                'memory_used': memory_used  # in kilobytes
            })

        # Calculate averages
        average_execution_time = total_execution_time / num_inputs if num_inputs > 0 else 0
        average_memory_used = total_memory_used / num_inputs if num_inputs > 0 else 0

        # Add average execution time and memory usage to the response
        summary = {
            'average_execution_time': average_execution_time,  # in seconds
            'average_memory_used': average_memory_used  # in kilobytes
        }

        # Return both detailed results and averages in the response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'results': results,
                'summary': summary
            })
        }

    except Exception as e:
        # Return the error message if something goes wrong
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({
                'event': event,
                'error': str(e)
            })
        }
