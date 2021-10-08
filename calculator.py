print("Calculator application. Please give me the")
print("1.operand (integer)")
operand1 = int(input())
print("operator (+ | - | * | /)")
operator = input()
print("2.operand (integer)")
operand2 = int(input())

if operator == '+':
    result = operand1 + operand2
elif operator == '-':
    result = operand1 - operand2
elif operator == '*':
    result = operand1 * operand2
elif operator == '/':
    result = operand1 / operand2

print(f'result: {result}')
