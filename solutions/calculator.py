"""
caluclator.py - has 4 basic functions: add, times, divide, minus
the calculator will take an innitial base number from the user
then run in a loop, carrying out opperations depending on what the user wants
the calculator should prompt separately for each number and function
"""

# function to add a number to the base
def add(number_to_add):
  base_number += number_to_add

# function to minus a number to the base
def minus(number_to_take):
  base_number -= number_to_take

# function to times a number to the base
def times(number_to_times):
  base_number *= number_to_times

# function to divide the base by a number
def divide(number_to_divide):
  base_number /= number_to_divide

# function to list all the options
def list():
  print(
  """add
  times
  minus
  divide
  quit
  """)

# provide a welcome message
print("welcome to calculator for a list of available opperations use 'list' ")

# get the base number, we still need this even if the user just wants to list
# or even quit
base_number = int(input("but first enter a number to start with > "))

# loop forever
while True:
  # ask for the opperation
  op = input("select operation > ")

  # ask for a second number to apply the operation with
  # if the operation is list or quit we only need them to continue with enter
  second_number = int(input("choose number to apply or return for list or enter > "))

  # check for each operation, call the function if the operation matches
  if op == "add":
    add(second_number)
  elif op == "times":
    times(second_number)
  elif op == "divide":
    divide(second_number)
  elif op == "minus"
    minus(second_number)
  elif op == "list":
    list()
  elif op == "quit":
    exit(0)
  # include a catch all if the user supplies an invalid operation
  else:
  raise Error("invalid opperation")
