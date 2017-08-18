
# parrot_loop.py

# print out a help message for the user
print("this program will repeat anything you say in a parrot fasion")
print("type quit or exit to end the program")

# get user input
user_input = input("say something > ")

# if the user doesn't quit, loop around printing the given input
# and prompting for more input
while user_input != "exit" and user_input != "quit":
  print("*squawk* " + user_input + " *squawk*")
  user_input = input("say something > ")
