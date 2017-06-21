#!/usr/env python3
################################################################################
# xor.py

# bellow we have 3 ways to do the same thing, consider how easy each method is
# to undestand just by reading

first_condition = True
second_condition = False

################################################################################

# using nested statements

# lets set the or part of the xor
if first_condition or second_condition:
  # if we get here either one or both condition are True, now we need to check
  # that not both conditions are true
  if not (first_condition and second_condition):
    # if we get to this point we have one and only one condition true - an xor
    print("this is an xor, only one condition is True")
  else:
    # if at least one condtion is True, but not only one, both must be True
    print("this is an and, both conditions are True")
else:
  # this is the else statement for the outer if, if we are here both are False
  print("neither condition is True")

################################################################################

# using elif
if first_condition and second_condition:
  print("this is an and, both conditions are True")
# if the first statement is False then we know not both conditions are True
# so now we only need to check if one is True
elif first_condition or second_condition:
  print("this is an xor, only one condition is True")
else:
  # the or part only needed one condition to be True so if that didn't execute
  # then neither condition is True
  print("neither condition is True")

################################################################################

# using just one if statement
# one condition or the other and noth both
if (first_condition or second_condition) and not (first_condition and second_condition):
  print("this is an xor, only one condition is True")
