#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    y = sys.argv

    if len(y) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if y[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(y[1])
    b = int(y[3])
    print("{} {} {} = {}".format(a, y[2], b, operators[y[2]](a, b)))
