# Extra credit

## Shorthand operators

A very common thing to do is to increment or decrement a variable for whatever
reason, say, counting something for example. This would be done like so.
```python3
number_of_balls = 6
print("there is " + number_of_balls + " balls")

input("Press [ENTER] to add a ball")

number_of_balls = number_of_balls + 1
print("there is " + number_of_balls + " balls")
```

In fact this is so common there is a shortcut to doing this, these are
shortcut operators.

| Operation | Short for  |
|:---------:|:----------:|
| x += y    | x = x + y  |
| x -= y    | x = x - y  |
| x *= y    | x = x * y  |
| x **= y   | x = x ** y |

So our example would be as follows.
```python3
number_of_balls = 6
print("there is " + number_of_balls + " balls")

input("Press [ENTER] to add a ball")

number_of_balls += 1
print("there is " + number_of_balls + " balls")
```
---
[Lesson04 - Operations](../lessons/Lesson04.md)
