# snakes_and_ladders.py
# we need argv from sys and randint from random
# argv is optional but it allows the setup to be done quicker


################################################################################
################################# CONSTANTS ####################################
################################################################################

# help message

# The most players allowed in a single game

# the smallest number a player can roll

# the largest number a player can roll

# the final location a player can land on, if they land here they win

################################################################################
################################## VARIABLES ###################################
################################################################################

# a boolean representing whether a player has won or not
# starts off True, when win(player_number) is called, this becomes False

################################################################################
############################### DATA STRUCTURES ################################
################################################################################

# Data Structures (snakes, ladders, players)
# The snakes and ladders are predefined

# a number of lists with two ints inside, the list represents the snakes
# the first element is the head of the snake and the second is the tail
# snake = [head_location, tail_location]

# a list containing all the snakes

# The same set of lists for the ladders
# ladder = [base_location, top_location]

# an empty list for the players

################################################################################
################################### FUNCTIONS ##################################
################################################################################

# setup function
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

  # let the user know what's happening

  # if the number of players is 0, prompt for the number of players

  # add as many players to the list as given

  # if the list is too long then the user added an illegal number
  # if thats the case clear the list and try again
  # if the list is okay, then we have a valid setup

  # do the same thing for non-zero values for number_of_players

  # don't forget to set the number_of_players to 0, to prevent an
  # infinte loop

# take turn function
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

  # the roll is a random number from DICE_MIN to DICE_MAX

  # tell the player the result use input for enter to continue behavior

  # work out where the user will land

  # make sure the user cant move over the WINNING_LOCATION
  # if they try, tell them they can't and return the previous location

  # check if the player has landed on any ladder base

  # if so, tell them and move them to the top of the ladder

  # check if the player has landed on a snake head

  # if so, tell them and move them to the snake tail

  # let the player know where they landed and return that number

# win function
  """
  The player this function is called with will be declared the winner.
  The function also sets the no_one_has_won variable to False, since the
  declared player has in fact won.
  """
  # we need to make the no_one_has_won variable global

  # print a congratulatory message for the winning player
  # make sure to include the player number

  # since someone has won, the no_one_has_won variable is False




################################################################################
################################### RUN ########################################
################################################################################

# Setup the game or display help

  # If an arguments are passed, it is either the help message
  # or the number of players

# Play the game

  # every player should take a turn

  # if no one has won then they go through with the turns

  # let players know a new round is starting

  # let the player whos turn it is know it's their turn

  # that player should then take a turn

  # if the player has made it to the WINNING_LOCATION then call
  # the win function the program should then end
