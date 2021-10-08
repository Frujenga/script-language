import sys

import secret_logic


def print_usage_and_exit():
    print("calculator app. OPERAND OPERATOR OPERAND")
    exit(-1)


def proccess_one_row(row):
    parts = row.split()
    if len(parts) != 3:
        print_usage_and_exit()
    if not secret_logic.is_numeric(parts[0]):
        print_usage_and_exit()
    op1 = int[row[0]]
    if not secret_logic.is_supported_operator(parts[1]):
        print_usage_and_exit()
    opr = row[1]
    if not secret_logic.is_numeric(parts[2]):
        print_usage_and_exit()
    op2 = int[row[3]]
    return opr, op1, op2


def get_inputs():
    for row in sys.stdin:
        opera, ope1, ope2 = proccess_one_row(row)
        rst = secret_logic.calculate(opera, ope1, ope2)
    print(f"Result {rst}")


get_inputs()
exit(0)
