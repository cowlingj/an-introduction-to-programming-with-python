"""
factorial.py - calculates the factorial of a given integer
"""

# n.b. factorial (symbol !) is a mathematical function,
# for any given positive integer, it's factorial will be
# numbers from - to it all multiplied together
# so 1! = 1,
# 2! = 2 * 1 = 2,
# 3! = 3 * 2 * 1 = 6,
# 4! = 4 * 3 * 2 * 1 = 24...

# get the number to apply factorial to
base_number = int(input("enter an integer to get the factorial: "))

factorial_so_far = 1

# accumulate the factorial in a loop
for index in range(1, base_number + 1):
  factorial_so_far = factorial_so_far * index

# print the factorial
print("factorial of " + str(base_number) + " is " + factorial_so_far)
