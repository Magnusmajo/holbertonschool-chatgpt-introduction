#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: python3 script_name.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("The number must be non-negative.")
    else:
        f = factorial(num)
        print(f"The factorial of {num} is {f}")
except ValueError:
    print("Please provide a valid integer number.")

