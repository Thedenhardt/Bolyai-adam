# define a list of valid operation signs
operations = ['+', '-', '*', '/']


# define a function to perform the calculator operations
def calculate(input_string):
    # initialize the operand variables
    operand1 = 0
    operand2 = 0
    operation = ''

    # iterate through the input string to extract the operands and operation
    for i, char in enumerate(input_string):
        # check if the character is a digit
        if char.isdigit():
            # check if the operation has been set
            if operation:
                # set the second operand
                operand2 = operand2 * 10 + int(char)
            else:
                # set the first operand
                operand1 = operand1 * 10 + int(char)
        # check if the character is an operation sign
        elif char in operations:
            # set the operation
            operation = char

    # perform the operation and return the result
    if operation == '+':
        return operand1 + operand2
    elif operation == '-':
        return operand1 - operand2
    elif operation == '*':
        return operand1 * operand2
    elif operation == '/':
        # check for division by zero
        if operand2 == 0:
            return "Cannot divide by zero"
        else:
            return operand1 / operand2
    else:
        return "Invalid operation"


# get the input from the user
input_string = input("Enter an operation (e.g. 2+3): ")

# calculate and print the result
result = calculate(input_string)
print(result)
