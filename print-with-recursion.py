"""
Given a positive integer n, write a function, print_integers, that uses recursion to print all numbers
from n to 1.

For example, if n is 4, the function should print 4 3 2 1.
"""


def print_integers(n):
    # TODO: Complete the function so that it uses recursion to print all integers from n to 1
    if n <= 0:
        return
    print(n, end="")
    print_integers(n-1)
    pass


print_integers(5)
