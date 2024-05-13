#!/usr/bin/python3
import sys

def factorial(n):
   """
    Function Description:
        Calculates the factorial of a non-negative integer.

    Parameters:
        n (int): The input integer for which to compute the factorial.

    Returns:
        int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
