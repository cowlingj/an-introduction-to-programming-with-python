#!/usr/env python3
################################################################################
# infinite_loop.py

# lets ask for a starting number
counter = int(input("count from this number to 5 "))

while counter <= 5:
  print(counter)
  # we missed out "counter = counter + 1"

# we will never get to this point if the user gives us a number less than 5
print("done")