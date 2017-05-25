#!/usr/bin/python3
import sys
try:
    fun = sys.argv[1]
    op1 = float(sys.argv[2])
    op2 = float(sys.argv[3])
except IndexError:
    print("3 arguments are needed")
    sys.exit()
except ValueError:
    print("Arguments have to be floats")
    sys.exit()

if fun == ("sumar"):
    result = op1 + op2
elif fun == ("restar"):
    result = op1 - op2
elif fun == ("multiplicar"):
    result = op1 * op2
elif fun == ("dividir"):
    try:
        result = op1 / op2
    except ZeroDivisionError:
        print("No possible divide 0")
        sys.exit()
else:
    print("Operator doesn't exist")
    sys.exit()

print("Resultado: " + str(result))
