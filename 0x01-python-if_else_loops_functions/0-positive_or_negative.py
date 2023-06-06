#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("Is negative")
elif number > 0:
    print("Is positive")
else:
    print("Is zero")
print(number)
