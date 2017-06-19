#!/usr/bin/env python3
################################################################################
# who_is_older.py

# get the first users name
user_1_name = input("User 1, please enter your name ")

# now get their age
user_1_age_string = input("hello " + user_1_name + "how old are you? ")
user_1_age_int = int(user_1_age_string)

# do the same thing for the second person
user_2_name = input("User 2, please enter your name")

# lets get their age too
user_2_age_int = int(input("hello " + user_2_name + "how old are you? "))
# this does the same thing as the two lines of code we wrote to get the first
# users age as an integer, because we can wrap functions inside functions,
# and the inner function is always evaluated first.

# now lets compare the ages, and say if the first user is older
if user_1_age_int > user_2_age_int:
  print(user_1_name + " is older")

# lets compare again, and say if the second user is older
if user_1_age_int < user_2_age_int:
  print(user_2_name + " is older")

# and now compare them to see if they are the same age
if user_1_age_int == user_2_age_int:
  print(user_1_name + " is the same age as" + user_2_name)

# print out a message telling the users the program is complete
print("comparason completed")