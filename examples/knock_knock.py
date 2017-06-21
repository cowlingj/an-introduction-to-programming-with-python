#!/usr/bin/env python3
################################################################################
# knock_knock.py

"""
This program tells a knock knock joke, and forces the user to play along.
If the user replies incorrectly the program will repeat that part of the joke
"""

# the first prompt and the appropriate response to the first prompt
FIRST_PROMPT = "knock knock\n> "
FIRST_CORRECT_INPUT = "who's there?"

# prompt the user with the usual start of a knock knock joke
first_input = input(FIRST_PROMPT)

# if the user doesn't reply correctly complain and then repeat
while first_input != FIRST_CORRECT_INPUT:
  print("Come on, that's not right")
  print("say " + FIRST_CORRECT_INPUT)
  first_input = input(FIRST_PROMPT)

# the next and final set of prompt and response (the joke setup)
SECOND_PROMPT = "lettuce\n> "
SECOND_CORRECT_INPUT = "lettuce who?"

# prompt the user with the setup part of the joke
second_input = input(SECOND_PROMPT)

# if the user doesn't reply correctly complain and then repeat
while second_input != SECOND_CORRECT_INPUT:
  print("Come on, that's not right")
  print("say " + SECOND_CORRECT_INPUT)
  second_input = input(SECOND_PROMPT)

# the punchline to the joke
PUNCH_LINE = "lettuce in it's cold"

# deliver the punch line
print(PUNCH_LINE)
