// export const handler = async (event) => {
//   try {
//     // Parse the request payload
//     const data = event
//     const code = data.code;
//     const inputSets = data.input_sets;
//     const expectedOutputs = data.expected_outputs;

//     if (!code) {
//       throw new Error("The 'code' field is missing from the payload.");
//     }

//     if (!Array.isArray(inputSets) || inputSets.length === 0) {
//       throw new Error("The 'input_sets' field should be a non-empty array.");
//     }

//     let totalExecutionTime = 0;
//     const results = [];

//     // Create a Function constructor with the provided code
//     const script = new Function('inputs', `
//       ${code};
//       if (typeof Solution !== 'function') {
//         throw new Error("The provided code does not define a function named 'Solution'.");
//       }
//       return Solution(inputs);
//     `);

//     // Execute the code for each set of inputs
//     inputSets.forEach((inputs, idx) => {
//       try {
//         const start = performance.now(); // Start timing

//         // Execute the script
//         const result = script(inputs);

//         const end = performance.now(); // End timing
//         const executionTime = (end - start) / 1000; // Convert to seconds
//         totalExecutionTime += executionTime;

//         // Compare with expected output
//         const expectedOutput = expectedOutputs[idx];
//         const isMatch = expectedOutput !== undefined ? result === expectedOutput : null;

//         // Record result for each input set
//         results.push({
//           input_set: inputs,
//           actual_output: result,
//           expected_output: expectedOutput,
//           is_match: isMatch,
//           execution_time: executionTime // in seconds
//         });
//       } catch (err) {
//         results.push({
//           input_set: inputs,
//           error: err.message,
//           execution_time: 0
//         });
//       }
//     });

//     // Calculate average execution time
//     const averageExecutionTime = totalExecutionTime / inputSets.length;

//     // Return detailed results and averages
//     return {
//       statusCode: 200,
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({
//         results,
//         summary: {
//           average_execution_time: averageExecutionTime // in seconds
//         }
//       })
//     };

//   } catch (error) {
//     // Handle any errors in execution
//     return {
//       statusCode: 500,
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({
//         error: error.message
//         // error: JSON.stringify(event)
//       })
//     };
//   }
// };


import { VM } from 'vm2';

export const handler = async (event) => {
  try {
    const code = event.code;
    const inputSets = event.input_sets || [];
    const expectedOutputs = event.expected_outputs || [];

    const results = [];
    let totalExecutionTime = 0;
    let totalMemoryUsed = 0;
    const numInputs = inputSets.length;

    const vm = new VM({
      timeout: 1000, // Set a timeout for execution
      sandbox: {} // Provide an empty sandbox or any context needed
    });

    for (let idx = 0; idx < numInputs; idx++) {
      const inputs = inputSets[idx];
      const args = Object.values(inputs); // Convert the object values to an array of arguments

      // Start timing
      const startTime = process.hrtime();

      let result;
      try {
        // Run the user's code in the VM
        vm.run(code);

        // Check if 'Solution' function exists in the user's sandbox
        if (typeof vm.sandbox.Solution === 'function') {
          // Use apply to spread arguments from the array
          result = vm.sandbox.Solution.apply(null, args);
        } else {
          result = "No 'Solution' function defined in the provided code.";
        }
      } catch (e) {
        result = `Error executing user code: ${e.message}`;
      }

      // End timing
      const endTime = process.hrtime(startTime);
      const executionTime = endTime[0] * 1000 + endTime[1] / 1e6; // Convert to milliseconds
      const memoryUsed = process.memoryUsage().heapUsed / 1024; // Convert to kilobytes

      totalExecutionTime += executionTime;
      totalMemoryUsed += memoryUsed;

      const expectedOutput = expectedOutputs[idx] || null;
      results.push({
        input_set: inputs,
        actual_output: result,
        expected_output: expectedOutput,
        is_match: expectedOutput !== null ? result === expectedOutput : null,
        execution_time: executionTime, // in milliseconds
        memory_used: memoryUsed // in kilobytes
      });
    }

    const averageExecutionTime = numInputs > 0 ? totalExecutionTime / numInputs : 0;
    const averageMemoryUsed = numInputs > 0 ? totalMemoryUsed / numInputs : 0;

    const summary = {
      average_execution_time: averageExecutionTime, // in milliseconds
      average_memory_used: averageMemoryUsed // in kilobytes
    };

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        results: results,
        summary: summary
      })
    };

  } catch (e) {
    return {
      statusCode: 500,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        event: event,
        error: e.message
      })
    };
  }
};
