#!/usr/bin/python3
for b in range(ord('z'), ord('a') - 1, -1):
    c = chr(b)
    if (ord('z') - b) % 2 == 0:
        c = c.upper()
    print("{}".format(c), end="")
