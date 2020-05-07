"""
Given a user's input of n, return a list of factorials from 0! to n!

Test cases:
0! = 1
1! = 1
2! = 1 x 2 = 2
3! = 1 x 2 x 3 = 6
4! = 1 x 2 x 3 x 4 = 24
5! = 1 x 2 x 3 x 4 x5 = 120
"""


# Helper method to test equality
def equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


# Todo: Create a function that produces the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# Todo: Test factorial function
equals(factorial(0),1)
equals(factorial(2),2)
equals(factorial(4),24)
equals(factorial(5),120)

# Todo: Request a number from the user
n=int(input('Please provide a number: '))

# Todo: Print a list of factorials from 0 to the given number

for i in range(n+1):
    print("factorial of {} is {}".format(i,factorial(i)))