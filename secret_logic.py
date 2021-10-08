def is_numeric(text):
    return text.isnumeric()

def is_supported_operator(text):
    return text in ['+','-', '*','/']


def calculate(operator, operand1, operand2):
    result = 0
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    return result
