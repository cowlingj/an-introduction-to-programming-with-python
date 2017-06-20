# Lesson 7

# Checking a condition Multiple Times

Lets say we want to make python count to 5 by making it decide whether or not
to print and increment, the code may look something like this:
```python
counter = 1

if counter <= 5:
  print(counter)
  counter = counter + 1
if counter <= 5:
  print(counter)
  counter = counter + 1
if counter <= 5:
  print(counter)
  counter = counter + 1
if counter <= 5:
  print(counter)
  counter = counter + 1
if counter <= 5:
  print(counter)
  counter = counter + 1
# the counter should be greater than 5 now, we can use an
# if-else statement to check
if counter <= 5:
  print(counter)
  counter = counter + 1
else:
  print("done")
```
So the program starts with an integer variable `counter` which starts at 1, and
if the `counter` is less than or equal to 5 it will print the `counter` variable
and set the variable `counter` to one greater than the current `counter`
variable (a process known as incrementation), we know after the if statement
has executed 5 times it should be done, so let's just show that with one final
if-else statement.

Okay so let's do the same thing, but instead of counting to 5, lets count to 10,
or 100, or 1000... That's a lot of code...
Or maybe lets have the user input a number and will will count from that number
to 5, but what if the user gives us a number much less than 5, or more than 5,
we don't know, so how many times do we write if statements?
And what if we need to change something in the if statements, that's going to
take a long time.

**There _has_ to be a better way**

## Loops

We can use loops in python to solve all the problems talked about, we can test a
condition, then if the condition is true we execute the body of the loop, after
that we go back to the condition and repeat this until it is false, at which
point we move on passed the loop.

Time so see that a loop in action then...

### While

```python

counter = int(input("count from this number to 5 "))

while counter <= 5:
  print(counter)
  counter = counter + 1

print("done")
```

**Much better!**

So **while** our `counter` variable is less than or equal to 5, we print the
current value of `counter` then we increment it by 1, and then we print "done"
when the loop is finished.

> If we forget to increment the `counter` variable, if the user gives a number
> less than 5, then it will always be less than 5, so everytime we come back to
> the condition in the loop it will be true, and the loop will repeat forever.
> This is an infite loop, and normally we _really_ want to avoid those.
> To see this in action checkout infinte_loop.py, but first make sure you
> know how to force the program to stop!

### For

Another type of loop is a for loop