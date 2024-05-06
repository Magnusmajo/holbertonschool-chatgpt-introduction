#!/usr/bin/python3

import sys

def factorial(n):
    result = 1
    for num in range(2, n + 1):
        result *= num
    return result

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(f"The factorial of {num} is {factorial(num)}")

