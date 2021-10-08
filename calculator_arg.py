import sys

import secret_logic


def print_usage_and_exit():
    print("calculator app. OPERAND OPERATOR OPERAND")
    exit(-1)


if len(sys.argv) != 4:
    print_usage_and_exit()

op1 = int[sys.argv[1]]
opr = sys.argv[2]
op2 = int[sys.argv[3]]

rst = secret_logic.calculate(opr, op1, op2)
print(f"Result {rst}")
exit(0)
