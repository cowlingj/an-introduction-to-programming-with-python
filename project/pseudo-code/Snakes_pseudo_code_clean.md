# Snakes and Ladders
---
## Data Structures

> I'm going to need somewhere to hold the details of snakes, ladders and players

```pseudo
List(List(snake_head, snake_tail), ... )
List(List(ladder_base, ladder_top), ... )
List(List(player_number, player_location))
```

---
## Basic Structure

> how is the game going to play out

```pseudo
setup()

While (no_one_has_won)
  for player in player_list
  takeTurn(player)
  If player_location == 100
    win(player)
```
---
## More Detail

> look at the game mechanics in a little more detail and expand
> on some parts

```pseudo
def setup()
  input(number of players)
  for player in range(number_of_players)
    player -> playerList -> player_number
    1 -> playerList -> player_location

  fillPreDefinedBoard()

setup()
display()

def take_turn(location)
  input(enter to roll)
  dieScore = randInt(DIE_MAX)
  if location + dieScore <= 100
    location += dieScore
    for Snake in Snake_list
      if snake[0] == location
      location = snake[1]
    for Ladder in ladder_list
      if ladder[0] == location
      location = ladder[1]
    return newLocation

def win(PlayerNo)
  displayCongratsMessage(PlayerNo)
  no_one_has_won = false

while (no_one_has_won)
  for player in player_list
   take_turn(player_location)
   If player_location == 100
   win(player)
```
