import operator

# Mapping from words to digits
word_to_digit = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

# Mapping from operations to functions
operations = {
    'add': "+",
    'sub': "-",
    'mul': "*",
    'rem': "%",
    'pow': "**"
}

# Function to parse words into numbers
def parse_number(word):
    parts = word.split('c')  # Split based on 'c'
    number_str = []
    for part in parts:
        if part in word_to_digit:
            number_str.append(str(word_to_digit[part]))
        else:
            return None  # Invalid part
    try:
        number = int(''.join(number_str))
        return number
    except ValueError:
        return None
    

def evaluate_expression(expression):
    tokens = expression.split()
    parsed_expression = []
    
    # First, convert all operands to numbers and verify operations
    for token in tokens:
        if token in word_to_digit:
            parsed_expression.append(word_to_digit[token])
        elif 'c' in token:  # Possible composite number like onectwoczero (120)
            number = parse_number(token)
            if number is not None:
                parsed_expression.append(number)
            else:
                return "expression evaluation stopped invalid words present"
        elif token in operations:
            parsed_expression.append(operations[token])
        else:
            return "expression evaluation stopped invalid words present"

    # Now that all tokens are parsed, we can evaluate the expression
    i = len(parsed_expression) - 1

    while i >= 0:
        token = parsed_expression[i]

        if token in operations.values():
            if i+2 < len(parsed_expression):
                operand1 = parsed_expression[i+1]
                operand2 = parsed_expression[i+2]

                if isinstance(operand1, int) and isinstance(operand2, int):
                    result = eval(str(operand1) + token + str(operand2))
                    parsed_expression = parsed_expression[:i] + [result] + parsed_expression[i+3:]
                    i -= 1
                else:
                    return "expression is not complete or invalid"
            else:
                return "expression is not complete or invalid"
        else:
            i -= 1

    if len(parsed_expression) == 1 and isinstance(parsed_expression[0], int):
        return parsed_expression[0]
    else:
        return "expression is not complete or invalid"
    
        
        

if __name__ == '__main__':
    print(evaluate_expression(input()))