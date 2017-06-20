#!/usr/bin/env python3
################################################################################
# weather.py

# a string representiing the weather, we could have go this from user input
weather = "overcast"

# using if and elif, do different things for many specific values of weather 
if weather == "sunny":
  print("i'm going to need sunscreen")
eliif weather == "cloudy" or weather == "overcast":
  print("where did the sun go")
elif weather == "rain":
  print("raindrops keep falling on my head")
elif weather == "snow":
  print("I think I will stay inside")
# add an else as a "catch all" at the end of the conditions
else
  print("I don't know what the weather is")
