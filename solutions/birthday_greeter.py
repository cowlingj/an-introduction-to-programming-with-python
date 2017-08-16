
# birthday_greeter.py

# get the users age
age = int(input("Enter your age today "))

# print an age specific birthday greeting for some ages
if age < 0:
  print("umm... i don't think so?")
elif age == 1:
  print("Wow it's your first birthday!")
elif age == 4:
  print("You'll be going to school this year (thank goodness)")
elif age == 10:
  print("look at you, in double figures")
elif age == 11:
  print("it's time for high school now")
elif age == 17:
  print("you're now old enough to drive!")
elif age == 18:
  print("now you are an adult... no it's not all it's cracked up to be")
# the general greeting if the user doesn't hapen to be one of the specific ages
else:
  print("Happy Birthday!")
