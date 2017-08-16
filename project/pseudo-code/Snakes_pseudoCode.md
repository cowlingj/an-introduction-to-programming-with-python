# Snakes and Ladders
---
## Data
List(List(SnakeHead, Tail), ... )
List(List(LadderBase, Top), ... )
List(List(PlayerNo, Location))
---
## Basic Structure

setup()

While (noOne has Won)
  for each Player in list
   takeTurn(Player)
   If Player location == 100
   win(player)

---
## More Detail
def setup()
  input(NoOfPlayers)
  players -> playerList -> names
  1 -> playerList -> Locations

  fillPreDefinedBoard()

setup()
display()

def takeTurn(location)
  input(enter to roll)
  dieScore = randInt(DIEMAX)
  if location + diescore <= 100
    location += dieScore
    foreach Snake in SnakeList
      if snake[0] == location
      location = snake[1]
    foreach Ladder in ladderList
      if ladder[0] == location
      location = ladder[1]
    return newLocation

def win(PlayerNo)
  displayCongratsMessage(PlayerNo)
  noOneHasWon = false

  While (noOne has Won)
    for each Player in list
     Playerlocation = takeTurn(PlayerLocation)
     If Playerlocation == 100
     win(player)


While (noOne has Won)
  for each Player in list
   takeTurn(Player)
   If Player location == 100
   win(player)

## Tiles?
|------|
|42  S1|
|123456|
|------|


  
