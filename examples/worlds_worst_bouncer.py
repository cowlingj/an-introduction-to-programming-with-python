#!/usr/bin/env python3
################################################################################
# worlds_worst_bouncer.py

# get the users age
age = int(input("Oi! kid... How old are you? "))

# the constant minimum age for entry to our bar
MINIMUM_AGE = 18

# compare the users age to the minimum age
# display a message depending on the result
if age < MINIMUM_AGE:
  print("go away")
else:
  print("welcome")
