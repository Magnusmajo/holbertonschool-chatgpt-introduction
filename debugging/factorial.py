#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n
    return result

f = factorial(int(sys.argv[1]))
print(f)

""" The factorial function was stuck in an infinite loop. This happens because the value of n is never decremented inside the while loop, so n remains greater than 1 indefinitely.
o fix this, you need to decrement n within the loop, so the loop will eventually terminate when n becomes 1 """

