import sys

import secret_logic

sys.argv

op1= int[sys.argv[1]]
opr =sys.argv[2]
op2= int[sys.argv[3]]

rst = secret_logic.calculate(opr, op1, op2)
print(f"Result {rst}")
exit(0)