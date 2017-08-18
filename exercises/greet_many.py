"""
Greeter.py - Will build a list of names and then greet them all in turn
"""

# we need an empty list of people to greet
people_to_greet = []

# we also need a boolean to control if we need to add more names
want_more_names = True

while want_more_names:
  people_to_greet.append(input("Enter the name of who you would like to greet: "))

  prompt = input("add more names y/n? ")

  if prompt == "y":
    print("continuing...")
  elif prompt == "n":
    print("beginning to greet")
    want_more_names = False
  else:
    print("not recognised, beginning to greet")
    want_more_names = False
