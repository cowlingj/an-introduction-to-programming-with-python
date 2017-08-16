
# guess_my_number.py

from random import randint

# get both users to guess a number
user_1_guess = int(input("I'm thinking of a number between 1 and 10, "
                         + "have a guess user 1 >"))

user_2_guess = int(input("Now user 2 guess >"))

# randomly generate a number between 1 and 10
answer = randint(1, 10)

# get the distance each user was from the answer
user_1_distance = answer - user_1_guess
user_2_distance = answer - user_2_guess

# make both values positive since it doesn't matter if too high or too low,
# only who is closer
if user_1_distance < 0:
  user_1_distance = user_1_distance * (-1)

if user_2_distance < 0:
  user_2_distance = user_2_distance * (-1)

if user_1_distance < user_2_distance:
  print("user 1 was closer, the answer was " + str(answer))
elif user_2_distance < user_1_distance:
  print("user 2 was closer, the answer was " + str(answer))
else:
  print("It's a draw, the answer was " + str(answer))
