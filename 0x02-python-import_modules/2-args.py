#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = sys.argv
    arg_len = len(a) - 1
    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
    for b in range(arg_len):
        print("{}: {}".format(b + 1, a[b + 1]))
