#!/usr/bin/python3
import random
number = -98
ld = int(str(number)[-1])
if (ld > 5):
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif (ld < 6 and ld != 0):
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {ld} and is 0")
