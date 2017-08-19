# Lesson 9

## mathematical Operators on Lists

Python has also defined operations that can be done on lists, lists can be added
together with the + operator.
```python
class_9A = ["adam", "bethany", "connor", "danielle"]
class_9B = ["amy", "brandon", "charlotte", "dylan"]
year_group_9 = class_9A + class_9B
print(year_group_9)
```
The * operator can be used between a list and an integer too, this is equivalent
to creating a new list of a number of copies of the supplied list all appended
to one another.
```python3
party_items_per_person = ["party hat", "balloon", "party popper"]
guests_at_party = 3
total_party_items = party_items_per_person * guests_at_party
print("I need to buy " + str(total_party_items)
```
The example creates a list `party_items_per_person` and uses the * operator to
create a new list `total_party_items` which consists of every element in
`party_items_per_person` three times like so: `total_party_items = ['party hat',
'balloon', 'party popper', 'party hat', 'balloon', 'party popper', 'party hat',
'balloon', 'party popper']`.

## Slicing

List slicing allows us to get sections of the list, or sub-lists from a list,
and works in a similar way to accessing an item in the list by an index, but
instead of using a single index, we use a range of indecies to give us a list.
```python3
sports = ["football", "basketball", "netball", "cricket", "tennis", "badminton",
          "athletics"]
ball_sports = sports[0 : -1]
team_sports = sports[0 : 4]
racket_sports = sports[4 : 6]

print("ball sports: " + str(ball_sports))
print("team sports: " + str(team_sports))
print("racket sports: " + str(racket_sports))
```
We use list slicing in the example above with the colon ":" symbol, the starting
index is the number before the colon and the ending index is after **note that
the sub-list does not include the item at the ending index**

> If we don't write anything before the colon, this is the same as specifying
> the first item. If we don't write anything after the colon, it is considered
> as the end of the list.

### Specifying the Increment

We can also choose to take every other item, or every third item, and so on by
adding a little more to our slice like so:
```python3
sports = ["football", "basketball", "netball", "cricket", "tennis", "badminton",
          "athletics"]
sports_i_watch = sports[ : 6 : 2]
sports_i_do = sports[-1 : 3 : -1]

print(sports_i_watch)
print(sports_i_do)
```
This example is a little more complicated and shows how we can choose our own
increment instead of just incrementing by 1, and and demonstrates slicing a list
backwards.

> Consider having separate lists of things that are closely related to avoid
> making mistakes with list slicing, and to make code simpler to think about

## Strings as Lists

Looking back at (lesson 2)[#], remember the definition we gave to a string:

> A string is a list of letters or characters...

Since a string is a list of characters, it should be no surprise that all of the
things we can do with lists, slicing, operations, functions, we can do on
strings too, feel free to experiment with some of the concepts covered in the
list sections with strings too.

## for Loop

Another type of loop is a **for** loop, this type of loop doesn't use a boolean
condition, instead it works by looking at each item in a list.
```python3
pet_store = ["spot", "rex", "luca", "oscar", "bob"]

for pet in pet_store:
  print(pet + " for sale")
```
The **for** loop creates a temporary variable to store a reference to an item in
a list, in the example we called this variable `pet` to reference each item in
`pet_store`, the **for** loop first uses `pet` to represent the first item, then
after the body executes once, it starts again with `pet` now referring to the
second item in `pet_store`. the loop ends after the last item has been
referenced.

## range

In python there is a function called range which takes in a number, and returns
a list of integers from 0 to the number given so `range(3)` would be the
integers `[0, 1, 2]`

We can supply two numbers to range and it will return a list of integers from
the first number to the second, `range(2, 7)` is `[2, 3, 4, 5, 6]`.

If we supply three numbers, the first is the start, the second is the end and
the third is the number to increment by - just like with list slicing, so
`range(2, 6, 2)` is `[2, 4]`.

---
**[Example06 - multiply_number_list.py](../examples/multiply_number_list.py)**  
**[Exercise09 - factorial.py](../exercises/factorial.py)**  

---
**[previous lesson](./Lesson08.md)**  
**[next lesson](./Lesson10.md)**
