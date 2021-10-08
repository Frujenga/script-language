import secret_logic


def ask():
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
    text = input()
    while not text.isnumeric():
        print("Bad input, again")
        text = input()
    operand2 = int(text)
    return operator, operand1, operand2


opr, op1, op2 = ask()
rst = secret_logic.calculate(opr, op1, op2)
print(f"Result {rst}")
exit(0)
