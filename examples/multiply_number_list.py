"""
multiply_number_list.py - takes a list of numbers and multiplys all of them
by another number
"""

# an empty list that will hold the numbers to be multiplied
list_to_multiply = []
# a boolean to control a loop to add numbers to the list
continue_adding_numbers = True

# loop adding numbers to the list
while continue_adding numbers:
  # prompt the user to add a number to a list
  number_to_add = float(input("add a number to the list to be multiplied: "))

  # prompt the user whether to continue or not
  prompt = input("add more numbers y/n? ")

   # depending on what the user wants, we may change the variable
   # controlling the loop
   if prompt == "y":
     print("continuing...")
   elif prompt == "n":
     continue_adding_numbers = False
   else:
     print("not recognised, quitting")
     want_more_names = False

# prompt the user for the number to multiply the list items with
number_to_multiply = float(input("enter a number to multiply the list with: "))

# use a for loop to loop around and multiply each item with the number
for number in list_to_multiply:
  print(str(number) + " -> " + str(number * number_to_multiply))
