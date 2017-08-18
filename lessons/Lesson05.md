# Lesson 5

## Booleans

A boolean is a data type that can have one of two values `True` or `False`,
this allows us to do certain things depending on which of those two values
a particular boolean is.
This may seem a little confusing now but it will make more sense in later
examples.

## Conditional Statements

A conditional statement is something we are all familiar with, for example:

_If you are hungry, then go and eat food._

Let's look at that statement in a little more detail:

_**If** you are hungry, then go and eat food._

  **If** - this word indicates there is some sort of condition.

_If **you are hungry**, then go and eat food._

  **you are hungry** - this is the condition, you are hungry can be either true,
  if you are hungry, or false if you are not hungry.

_If you are hungry, **then go and eat food.**_

  **then go and eat food.** - this is the body of the statement, the "stuff"
  that needs to be done if the condition is met.

## Conditional Statements in Python

Let's look at an example in code then:
```python3
food = 5
hungry = False

if hungry:
  food = food + 1

print(food)
```
> common errors in example like these include syntax errors, from forgetting the
> colon ":" at the end, or an Indentation Error caused by not indenting the body
> with either tabs or spaces (either is fine so long as you are consistent)

In this example we have two variables, `food` which is currently the integer `5`,
and `hungry` which is the boolean value `False` (always with a capital "F" in
python).
If the condition `hungry` is `True` (it's not) then we go into the body and
assign the variable `food` the value of `food + 1`.
The final output will be 5 then, try changing the boolean in the example (hungry.py)
to see how that affects the output.

## Logical Operators

We can directly assign booleans like in the example above or we can create them
by making comparasons with logical operators that we are all familiar with
already:
* greater than
* less than
* equal to
* not
* and
* or

The logical operators have the following symbols and descriptions:

| Name         | Symbol | Description                                                  |
|:------------:|:------:|:------------------------------------------------------------:|
| greater than | >      | if the first operand is greater than the other, this is True |
| less than    | <      | if the first operand is less than the other, this is True    |
| equal to     | ==     | if the first operand is the same as the other this is True   |
| not          | not    | this is the oposite to the single boolean value it gets      |

> remember the **assignment opperator** is a single equals sign **"="** while
> the logical operator **equals** is two equals signs **"="**

We can use these operators to get boolean results like in the following example:
```python3
my_boolean = 1 < 2
my_other_boolean = 1 > 2
```
In the example the `my_boolean` is `True` since 1 is in fact less than 2, so the
variable `my_other_boolean` must be false, since 1 is obviously not greater than
2.

### More Logical Operators

There are a few ways we can combine the above operators to do some more logic.
Lets look at these extra operators:

| Name                     | Symbol |
|:------------------------:|:------:|
| greater than or equal to | >=     |
| less than or equal to    | <=     |
| not equal to             | !=     |

These work like the others do, in pretty much the same way, lets look:
```python3
my_dogs_weight = 40
my_cats_weight = 10
weights_differ = my_dogs_weight != my_cats_weight
```
And as you would expect, `weights_differ` is `True`.

## Expressions in Conditional Statements

Just as we can do `print(3 + 5)`, we can also do
```python3
if 3 == 5:
  print("the world is ending")
print("i am outside of the condition")
```
## Comparing Strings

The logical operators have meaning used with strings, greater than and less than
compare the number of characters in both strings **including whitespace and
punctuation**, while equals compares the contents of the strings.
```python3
my_dogs_name = "Mrs Barks a lot"
my_cats_name = "Mr also barks a lot, because cat's are weird"

if my_cats_name > my_dogs_name:
  print(my_cats_name + " name is longer")
```
The example will print out `Mr also barks a lot, because cat's are weird name is
longer`.

## Common Conditional Statement Bad Habbit

Many new programmers fall into the trap of doing an extra comparason with
conditional statements using a single variable.
Take the earlier hungry.py example:
```python3
food = 5
hungry = False

if hungry:
  food = food + 1

print(food)
```
Many new programmers make the mistake of writing:

```python3
food = 5
hungry = False

if hungry == True:
  food = food + 1

print(food)
```
In the line which reads `if hungry == True:` an extra comparason has been made.
the boolean hungry is either `True` or `False` so there is no need to find out
whether `True == True` or `False == True` because this has the exact same effect
as just using the boolean alone.
Even though they reach the same answer it adds an extra step, and more
experienced programmers hate it (I may be one of them).

> It may seem a poor reson not to write code a certain way because programmers
> don't like it, but consider programs written in industry are read many, many
> times, so it's important that it is easy to read.

---
**[Example03 - hungry.py](../examples/hungry.py)**  
**[Exercise05 - who_is_older.py](../examples/who_is_older.py)**  

---
**[previous lesson](./Lesson04.md)**  
**[next lesson](./Lesson06.md)**  
