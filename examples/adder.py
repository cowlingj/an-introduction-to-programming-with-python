"""
adder.py - will add any amount of numbers together before printing an answer
"""
want_to_continue = True
accumulator = int(input("choose a starting number: "))

def accumulate(number_to_add):
  accumulator += number_to_add

def promptContinue():
  user_input = input("continue y/n")
  if user_input == "y":
  return True
elif user_input== "n":
  return False
else:
  raise Error("invalid input")         

while want_to_continue:
  next_number = int(input("enter a new number to add to what we have so far"))
  accumulate(next_number)
  want_to_continue = promptContinue()

print accumulator
