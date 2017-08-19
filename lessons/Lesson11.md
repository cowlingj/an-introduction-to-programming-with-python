# Lesson 11

## Functions

We have already used functions in this course such as **print** and **input**,
but what exactly are they and can we create something like that?

A function is a way to split code, by giving a name to a specific section we
can use that section when ever we need to. This means we don't have to repeat
ourselves while writing code - which is very important in the world of
programming.

## defining functions

We define a function using the **def** keyword, and giving the function a name
(the same rules for naming variables apply), followed by a pair of brackets.
The lines of code that are part of the function should be an indented block.
```python3
def say_hello()
  print("hello - this is my first function")

say_hello()
```
functions allow us to execute that block of code anywhere just by calling its
name.

## parameters

We can pass arguments to functions we write, just ass we did with the built in
functions, all we need to do is specify variables inside the brackets (these are
called parameters), use them as normal variables inside the code,
then pass in the variables when we want to use the function.

> To clarify the difference between parameters and arguments:
> we pass arguments to a function
> a function can have parameters
> (so parameters act as placeholders for arguments)
```python3

magic_number = 6

def area_of_a_square(side_length):
  area = side_length * side_length
  print("A square of length " + side_length + " has an area of " + area)

area_of_a_square(2)

area_of_a_square(4)

area_of_a_square(magic_number)

area_of_a_square(532)
```

> For anyone wondering python uses pass by value, so you don't need to worry
> about variable being changed by a function - unless you use **global**,
> which is often a bag idea.

Just as with built in functions we can separate parameters with commas.

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
return statement are unlikely to be executed.

> We can call functions in assignments to assign a variable the result, or even
> call functions as arguments to other functions, passing across the return
> value

## Global

If we don't name a variable in a function then we cannot access it at all, this
behaviour is unlike many other languages. But inside a function referencing a
variable from the outside of that function is a little different.
We need to declare it as global first.
```python3
predefined_string = "this string was defined outside the function"

def print_predefined_string:
  global predefined_string
  print(predefined_string)
```

---
**[Example08 - adder.py](../examples/adder.py)**  
**[Exercise11 - calculator.py](../exercises/calculator.py)**  

---
**[previous lesson](./Lesson10.md)**  
**[next lesson](./Lesson12.md)**
