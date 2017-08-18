"""
adder.py - will add any amount of numbers together before printing an answer
"""
# a boolean to control the loop
want_to_continue = True
# the number we are using to accumulate each number to add
# starts at whatever the user chooses as the first number
accumulator = int(input("choose a starting number: "))

# accumulate function will add a given number to the accumulator
def accumulate(number_to_add):
  accumulator += number_to_add

# a function that will prompt the user whether or not to continue
# if an invalid input is given the program will exit
def promptContinue():
  user_input = input("continue y/n")
  if user_input == "y":
  return True
elif user_input== "n":
  return False
else:
  print("Error: Invalid Input")
  exit(1)

# a function that will loop while the user wants to continue
while want_to_continue:
  # prompt the user for the next number
  next_number = int(input("enter a new number to add to what we have so far"))
  # accumulate the next number
  accumulate(next_number)
  # find out if the usewr wants to contine by prompting for continue
  want_to_continue = promptContinue()

# after print out the accumulator
print(accumulator)
