"""
Greeter.py - Will build a list of names and then greet them all at once
"""

# we need an empty list of people to greet
people_to_greet = []

# we also need a boolean to control if we need to add more names
want_more_names = True

# loop while we still want names
while want_more_names:
  # prompt for another name for us to add to the list of people to greet
  people_to_greet.append(input("Enter the name of who you would like to greet: "))

  # prompt to ask whether or not to continue adding names
  prompt = input("add more names y/n? ")

  # depending on if the user wants to add more we may change our variable
  if prompt == "y":
    print("continuing...")
  elif prompt == "n":
    print("beginning to greet")
    want_more_names = False
  else:
    print("not recognised, beginning to greet")
    want_more_names = False

# do the actual greeting, we can print a list of strings directly,
# like we would print any other non string type with str(LIST_NAME)
print("greetings to " + str(people_to_greet))
