# Lesson 8

## Lists

Lists are another data type, they are used to store related data, lets think
about a list were all familiar with first, a shopping list.
This shopping list can be considered a list of strings, so instead of having
a variable assigned to each item in the shopping list, it would make more sense
to have a variable for the shopping list and refrence a particular item on the
list when we need to.

## Lists in Python

We can create a list in python like so:
```python
shopping = ["spam", "eggs", "coffee", "chocolate"]
```
And there we have a list, the square brackets "[]" tell python that this
variable is a list, and we separate each item with commas.

We can access items in a list by refering to their position in the list,
otherwise known as an index.
```python
first_item_to_buy = shopping[2]
print("I need to buy " + first_item_to_buy)
```
This example will print out the item at index 2. But if you run this example
you will see `I need to buy coffee` as the output, why is this?
It is extremely common for programmers to begin counting from 0, this stems from
a history of very limited memory and resources and not wanting to waste any.
So in our example, the first item `"spam"` has an index of 0, `"eggs"` has an
index of 1, `"coffee"` an index of 3, and`"chocolate"` 4.

Trying to access index 5 will cause an error since ther is no item with that
index, but an index of -1 refers to the last element, -2 the second to last
element and so on.

In practice, creating and accessing items in a list looks like this:
```python
shopping = ["spam", "eggs", "coffee", "chocolate"]

first_item_to_buy = shopping[2]
first_item_in_list = shopping[0]
last_item_in_list = shopping[-1]
the_only_item_left = shopping[-3]

print("I need to buy " + first_item_to_buy + " first")
print("Then I must buy " + the_only_item_left + " for late nights coding")
print("After I should try the new " + last_item_in_list)
print("And finally I need to buy " + first_item_in_list)

```

## appending, inserting, removing, and length

We can do more with lists then just make them and get items from them, we can
get the length of a list by passing it to a function.

### len

The **len** function takes in a list and gives us the number of items in that list.
```python
shopping = ["spam", "eggs", "coffee", "chocolate"]
list_length + len(shopping)
print("I need to buy " + list_length + " items")
```
In the example a list called `shopping` is made containin 4 items, the length
of the list is found using the **len** function, and finally a line is printed
telling the user how many items to buy.

### append

Appending an item looks a little different to the functions seen so far, the
reason behind this is because of something called **object oriented
programming**, we won't cover this in the course, but we don't need to in
order to use these functions.

```python
shopping = ["spam", "eggs", "coffee"]

print("shopping list currently " + len(shopping) + " long")

shopping.append("chocolate")

print("now the shopping list is " + len(shopping) + " long")
```
> We can think of appending to a list as calling the function
> `append("chocolate")` but python doesn't know what list to add it to,
> so we first specify the list with `shopping` then we attach
> `append("chocolate")` onto that list with a dot `.` to give us
> `shopping.append("chocolate")`.

What **append** does is add the item to the end of the list. 

### remove

Removing an item is pretty similar, we just call the **remove** function in the
same way.

```python
shopping = ["spam", "eggs", "coffee", "chocolate", "oranges"]

print("The last item in the list is " + shopping[-1])

shopping.remove("oranges")

print("But now the lat item is " + shopping[-1])
```

We call the **remove** function with `"oranges"` on the list called `shopping`.

### insert

The **insert** function is similar to the append function, however the insert
function inserts an item at a particular position.
This means we must pass two things to the **insert** function, the position to
insert the item at and the item to insert, this can be done like so:
```python
compass_directions = ["north", "east", "south", "west"]
print(compass_directions)
compass_directions.insert(1, "north-east")
print(compass_directions)
compass_directions.insert(3, "south-east")
print(compass_directions)
compass_directions.insert(5, "south-west")
print(compass_directions)
compass_directions.insert(7, "north-west")
print(compass_directions)
```
The example creates a list and inserts 4 items one by one, printing the list
bettween each insert.

> There are some other useful functions on lists in python like **find** and
> **index**, we won't cover them in this course but feel free to find out about
> them,(click here)[https://docs.python.org/3/tutorial/datastructures.html] to
> look at some more list functions.
---
ADD STUFF HERE
