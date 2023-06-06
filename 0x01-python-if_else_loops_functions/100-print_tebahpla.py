#!/usr/bin/python3
for b in range(ord('z'), ord('a') - 1, -1):
    a = chr(b)
    if (ord('z') - b) % 2 == 1:
        a = a.upper()
    print("{}".format(a), end="")
