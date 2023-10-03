#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num1 = abs(number) % 10
if number < 0:
    num1 = -num1
print("Last digit of {} is {} and is ".format(number, num1), end="")
if num1 > 5:
    print("greater than 5")
elif num1 == 0:
    print("0")
else:
    print("less than 6 and not 0")
