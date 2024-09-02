#!/usr/bin/python3
import sys

for i in range(1, len(sys.argv)):
    print(sys.argv[i])

"""he error was that the index in Python starts at 0, so when using range(len(sys.argv)), it is iterating over all the elements of the list, including the script name itself (which is the first element, at index 0). This may not be what is desired, as it is generally not wanted to print the script name."""

"""
Another more elegant way to do it is by using list comprehension:
import sys

print(*sys.argv[1:], sep='\n')

In this case, sys.argv[1:] returns a list with all the elements of sys.argv except the first one (the script name). The * is used to "unpack" the list and pass each element as a separate argument to the print() function. The sep='\n' is used to print each element on a separate line."""
