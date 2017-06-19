__1. What does an assigment statement do?__

An assignment statement __asigns__ a value to a variable name.

__2. What is a String?__

A String is a sequence of characters.

__3. What data type is 2.718?__

2.718 is a float (or floating point decimal).

__4. What is the difference between 4 and 4.0?__

4 is an integer while 4.0 is a float (although python normally lets us ignore
this difference)

__5. Consider the following:__
```python
my_name="monty"
print("my_name")
```
__The program should print "monty", but instead prints "my_name", why is this?__

This happens because "my_name" is given to the print function with quotes,
meaning the string literal "my_name" is printed, to print the variable `my_name`
it shoud be given to print without quotes like this:
```python
print(my_name)
```