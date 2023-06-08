#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = sys.argv
    res = 0
    for b in range(len(a) - 1):
        res += int(a[b + 1])
    print("{}".format(res))
