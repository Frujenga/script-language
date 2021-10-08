print("Calculator application. Please give me the")
print("1.operand (integer)")
text = input()
while not text.isnumeric():
    print("Bad input, again")
    text = input()
operand1 = int(text)

print("operator (+ | - | * | /)")
text = input()
while text not in ['+', '-', '*', '/']:
    print("Bad input, again")
    text = input()
operator = text

print("2.operand (integer)")
while not text.isnumeric():
    print("Bad input, again")
    text = input()
operand2 = int(text)

if operator == '+':
    result = operand1 + operand2
elif operator == '-':
    result = operand1 - operand2
elif operator == '*':
    result = operand1 * operand2
elif operator == '/':
    result = operand1 / operand2

print(f'result: {result}')
exit(0)
