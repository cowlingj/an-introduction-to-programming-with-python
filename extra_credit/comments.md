# Extra Credit

## Comments

A comment is a piece of information that the interpreter ignores.
They allow us to pass information to programmers reading our code (including
ourselves, since we will be reading our code a lot).
We can explain how parts of code work using comments, which makes it easier to
read the code and understand what's going on (especially if we make a mistake
and our comment says that we are doing something we're not).

> But don't our variable names get across our intentions?
> Yes, to an extent, but we shouldn't just rely on this
> Good comments, _explain_ what a variable does, and how it is used, a variable
> name, just describes what it is

**Good comments are good practice, but require practice**

## Comments in Python

In python we have two types of comment, single line and multi line:
```python3
# This is a single line comment, none of this is read by the interpreter
# we can start single line comments with the "#" symbol
print("this is read by the interpreter") # this however isn't read
""" This is a multi line comment,
Everything between the three sets of quotes is ignored
print("so this is ignored")
"""
print("but this isn't ignored") # here's another end of line comment
```
Single line comments start with the **#** symbol, everything after the **#** is
ignored, so we can put single line comments at the end of a line with code we
want to run or on a line of its own.

Multi line comments sit between two sets of triple quotes *""" [COMMENT] """*,
we can write short multi line comments on a single line
`""" this is a short multi line comment """`.
However when using multi line comments, they must go on seperate lines to our
code that we want to run.

##  What to Comment

So comments are brilliant, but where should we use them?
The short answer is everywhere we can.
Comments are typically found at the start of files, to get the intention of the
file across; at the start of functions, to explain what they do; with variables,
if the variable's use isn't completely clear; and with blocks of code to explain
what should happen and why.

## Commenting out Code

We can also use comments to stop code being executed, which is great for bug
fixing, replacing code carefully, or for looking at how something works.
We call this code "commented out".
```python3
# print("this old thing doesn't look good")
print("but this line is beautiful")
```
When commenting out code, remember to either uncomment or delete the commented
out code completely - don't leave it in.

---
Exercise - bug_fix.py
