#!/usr/bin/env python3
################################################################################
# parrot.py

# use the input function to get user input
# n.b this was raw_input() in python 2.x
user_input = input("Say something... ")

# now lets print that input in a parrot like fasion
# don't forget to add spaces to seperate the variable from the strings
parrot_output = "*squak* " + user_input + " *squak*"
print(parrot_output)
