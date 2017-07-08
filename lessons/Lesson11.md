# Lesson 11

## Functions

We have already used functions in this course such as **print** and **input**,
but what exactly are they and can we create something like that?

A function is a way to spilit code, by giving a name to a specific section we
can use that section when ever we need to. This means we don't have to repeat
ourselves while writting code - which is very important in the world of
programming.

## defining functions

We define a funtion using the **def** keyword, and giving the function a name
(the same rules for naming variables apply), followed by a pair of brackets.
The lines of code that are part of the function should be an indented block.
```python3
def say_hello()
  print("hello - this is my first function")

say_hello()
```
functions allow us to execute that block of code anywhere just by calling its
name.

## paramiters

We can pass arguments to functions we write, just ass we did with the built in
functions, all we need to do is specify variables inside the brackets (these are
caled paramiters), use them as normal variables inside the code,
then pass in the variables when we want to use the function.
```python3
def area_of_a_square(side_length):
  area = sidelength * side_length
  print("A square of length " + side_length + " has an area of " + area)

area_of_a_square(2)

area_of_a_square(4)

area_of_a_square(532)
```

> For anyone wondering python uses pass by value, so you don't need to worry
> about variable being changed by a function - unless you use **global**,
> which is often a bag idea.

Just as with built in functions we can seperate paramiters with commas.

## return

However notice that with built in functions we can actually get a value from
them, take **input** for example, when we use this function, it gives us a
string - how can we get this functionality?

With a return statement.

```python3

def square_details(detail, side_length):
  if detail = "area":
    area = side_length * side_length
    return area
  elif detail = "perimeter":
    perimeter = side_length * 4
    return perimeter

square_area_size_3 = square_details("area", 3)
square_area_size_4 = square_details("area", 4)
square_area_size_5 = square_details("area", 5)

print("did you know the sum of squares 3 and 4 is the sum of the square 5?\n"
      + "look at this: \n"
      + "  square 3: " + str(square_area_size_3)
      + " + square 4: " + str(square_area_size_4)
      + " = square 5: " + str(square_area_size_5))
```
So all we need to do to return a value is use the keyword return followed by the
value.
When this happen the function ends and passes that value back, so things after a
retuen statement are unlikely to be executed.

---
ADD STUFF HERE!!!
