# bug_fix.py

"""
Program demonstrates how small details can cause bugs, and shows a basic
approach to solving bugs, as we gain more experience in programming and bug
fixing, we will find more ways to solve bugs - but this is a good place to
start.

NOTE TO BUG FIXER: try running the program with some simple cases, I've included
some bellow (and why i chose them), when trying to find out where the problem
is, a basic approach would be to check variables are what we expect them to be.
How can we find out what a variable is?
Print it out


CASES:
FIRST_NUMBER = 1, SECOND_NUMBER = 3 <- 2nd larger, middle is a whole number
FIRST_NUMBER = 1, SECOND_NUMBER = 2 <- 2nd larger, middle is a decimal
FIRST_NUMBER = 1, SECOND_NUMBER = 1 <- same size, middle = 2nd = 1st
FIRST_NUMBER = 2, SECOND_NUMBER = 1 <- 1st larger, middle is a decimal
FIRST_NUMBER = 3, SECOND_NUMBER = 1 <- 1st larger, middle is a whole number
"""

# The program takes two numbers and outputs the number exactly between them

# first we need the two numbers
FIRST_NUMBER = int(input("first number: "))
SECOND_NUMBER = int(input("second number: "))

# we can work out the middle by adding half of the difference to the smallest
# number, remembering the difference is always positive
DIFFERENCE = FIRST_NUMBER - SECOND_NUMBER

# to know which number to add to we just need to test which is smaller
# if they are equal then we can add to either number
if FIRST_NUMBER < SECOND_NUMBER:
  print("Middle: " + FIRST_NUMBER + DIFFERENCE)
else:
  print("Middle: " + SECOND_NUMBER + DIFFERENCE)
