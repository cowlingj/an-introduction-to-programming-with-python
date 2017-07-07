#!/usr/bin/env python3
# we need argv from sys and randint from random
# argv is optional but it allows the setup to be done quicker
from sys import argv
from random import randint
"""Snakes and Ladders"""

################################################################################
################################# CONSTANTS ####################################
################################################################################


# help message
HELP_MESSAGE = """Join with friends to play a game of snakes and ladders.
usage: snakes_and_ladders.py [-h|--help] [-p|--players <number_of_players>]"""

# The most players allowed in a single game
MAX_NUMBER_OF_PLAYERS = 6

# the smallest number a player can roll
DICE_MIN = 1

# the largest number a player can roll
DICE_MAX = 6

# the final location a player can land on, if they land here they win
WINNING_LOCATION = 100

################################################################################
################################## VARIABLES ###################################
################################################################################

# a boolean representing whether a player has won or not
# starts off True, when win(player_number) is called, this becomes False
no_one_has_won = True


################################################################################
############################### DATA STRUCTURES ################################
################################################################################


# Data Structures (snakes, ladders, players)
# The snakes and ladders are predefined

# a number of lists with two ints inside, the list represents the snakes
# the first element is the head of the snake and the second is the tail
# snake = [head_location, tail_location]
snake1 = [99, 61]
snake2 = [71, 49]
snake3 = [55, 37]
snake4 = [54, 32]
snake5 = [38, 27]
# a list containing all the snakes
snake_list = [snake1, snake2, snake3, snake4, snake5]

# The same set of lists for the ladders
# ladder = [base_location, top_location]
ladder1 = [10, 36]
ladder2 = [28, 47]
ladder3 = [41, 58]
ladder4 = [60, 85]
ladder5 = [69, 80]
ladder_list = [ladder1, ladder2, ladder3, ladder4, ladder5]

# an empty list for the players
player_list = []

################################################################################
################################### FUNCTIONS ##################################
################################################################################

def setup(number_of_players):
  """
  Setup the number of players.
  If the number_of_players variable given to it is 0, then prompt for the number
  of players.
  If the variable is 1 - 6 inclusive, then add that many players to the
  player_list.
  If the variable is something else, then the setup will loop
  """
  # if the game has been setup correctly, this is True.
  # changed to True in function setup(number_of_players)
  valid_setup = False
  while not valid_setup:
    # let the user know what's happening
    print("setting up...")
    # if the number of players is 0, prompt for the number of players
    if number_of_players == 0:
      real_number_of_players = int(input("how amany players (1 - 6): "))
      # add as many players to the list as given
      for player_number in range(real_number_of_players):
        player_list.append([player_number + 1, 1])
      # if the list is too long then the user added an illegal number
      # if thats the case clear the list and try again
      # if the list is okay, then we have a valid setup
      if len(player_list) <= MAX_NUMBER_OF_PLAYERS:
        valid_setup = True
      else:
        player_list.clear()
    else:
      # do the same thing for non-zero values for number_of_players
      for player_number in range(number_of_players):
        player_list.append([player_number + 1, 1])
      if len(player_list) <= 6:
        valid_setup = True
      else:
        # don't forget to set the number_of_players to 0, to prevent an
        # infinte loop
        player_list.clear()
        number_of_players = 0

def take_turn(location):
  """
  The function represents taking a turn in the game.
  The function takes a single paramiter, the location of the player taking the
  turn.
  First the player is prompted to press enter.
  Next a random number between 1 and 6 (inclusve) is chosen.
  This number is added to the player's location.
  If the result is either the start of a snake or a ladder then the end of the
  snake or ladder is the new location which is returned.
  If not the result of the addition is the new location which is returned.
  """
  # prompt "enter to roll"
  input("Press enter (\u23CE) to roll... ")
  # the roll is a random number from DICE_MIN to DICE_MAX
  die_roll = randint(DICE_MIN, DICE_MAX)
  # tell the player the result use input for enter to continue behavior
  input("Rolled " + str(die_roll))
  # work out where the user will land
  new_location = location + die_roll
  # make sure the user cant move over the WINNING_LOCATION
  # if they try, tell them they can't and return the previous location
  if new_location > WINNING_LOCATION:
    print("player cannot move, location would be " + str(new_location))
    input("actual location is still " + str(location))
    return location
  # check if the player has landed on any ladder base
  for ladder in ladder_list:
    if new_location == ladder[0]:
      # if so, tell them and move them to the top of the ladder
      input("Horray, you hit a ladder at " + str(new_location))
      new_location = ladder[1]
  # check if the player has landed on a snake head
  for snake in snake_list:
    if new_location == snake[0]:
      # if so, tell them and move them to the snake tail
      input("Oh no, you hit a snake at " + str(new_location))
      new_location = snake[1]
  # let the player know where they landed and return that number
  input("player moved to " + str(new_location))
  return new_location

def win(player_number):
  """
  The player this function is called with will be declared the winner.
  The function also sets the no_one_has_won variable to False, since the
  declared player has in fact won.
  """
  # we need to make the no_one_has_won variable global
  global no_one_has_won
  # print a congratulatory message for the winning player
  # make sure to include the player number
  print("VICTORY!!!")
  print("Player " + str(player_number) + " has won, congratulations")
  # since someone has won, the no_one_has_won variable is False
  no_one_has_won = False



################################################################################
################################### RUN ########################################
################################################################################

# Setup the game or display help

# If an arguments are passed, it is either the help message
# or the number of players
if argv[1] == "--help" or argv[1] == "-h":
  print(HELP_MESSAGE)
  exit(0)
elif argv[1] == "-p" or argv[1] == "--players":
  setup(int(argv[2]))
else:
  setup(0)

# Play the game
  # every player should take a turn
  for player in player_list:
    # if no one has won then they go through with the turns
    while no_one_has_won:
      # let players know a new round is starting
      print("\n\n\nnew round...\n\n\n")
      # let the player whos turn it is know it's their turn
      print("player " + str(player[0]) + ", it's your turn")
      # that player should then take a turn
      player[1] = take_turn(player[1])
      # if the player has made it to the WINNING_LOCATION then call
      # the win function the program should then end
      if player[1] == WINNING_LOCATION:
        win(player[0])
