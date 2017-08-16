# Extra Credit

## Error Handling

You may find in python that if something is written incorrectly an error message
will be shown, an error is also shown if an attempt is made to divide by 0.
This lets the programmer or user know we have done something wrong. We can
include errors in our own programs and we can also handle errors we get and try
to recover.

> Common terminology includes throwing an exception when something generates an
> exception and, catching an exception, which is where the exception is handled.
> The difference between an error and an exception, is the fact an error is
> something wrong with how the program is written, while an exception is an
> exceptional circumstance where something happens which shouldn't (however
> pythons standard exceptions and errors don't clearly make this distinction,
> here we will then refer to both errors and exceptions as exceptions)

## Recovering

We can recover from exception using **try** and **except**.
If we want to carry out something that could possibly cause an exception we use
**try**, if there is an exception then the try block immediately exits to the
**except** block, without executing any further code in the **try** block.
The except block then executes only if there is an exception.

In the example below, we prompt the user for an integer, if they do not provide
one then we get an exception, we handle this with an except statement, telling
the user what they did wrong.
```python3
try:
  int(input("input an integer... "))
except:
  print("you did not input an integer")
```

We can use multiple except blocks to handle different types of exception, such
as ValueError and IOError. We provide the type of exception to the except block,
if the type is not provided then the except statement handles all exceptions.
```python3
try:
  var file_to_read = open("myFile.txt")
  print(10 / int(file_to_read.readLine()))
  file_to_read.close()
except ZeroDivisionError:
  print("you cannot divide by 0")
except ValueError:
  print("the file does not contain an integer")
except IOError:
  print("cannot open the file")
except:
  print("something else broke")
```
The example above shows multiple except statements, some example of errors that
can be thrown include: IOError, OSError, SystemExit, ValueError, RuntimeError,
and more (for a more complete list
[click here](https://www.tutorialspoint.com/python/standard_exceptions.htm)).

### Finally

We can use a **finally** statement to execute any clean up code, or code that
we want to run after the **try except** block.
```python3
try:
  var file_to_read = open("myFile.txt")
  10 / int(file_to_read.readLine())
  # if we get here then everything so far works
  status = "OK"
except ZeroDivisionError:
  var status = "divide by 0"
except ValueError:
  var status = "no integer"
except IOError:
  var status = "cannot open the file"
except:
  var status = "something else broke"
finally:
  file_to_read.close()
  print(status)
```
In the example above we clean up by closing the file and then we print the
status.

## Throwing Errors

We can throw exceptions ourselves by using the **raise** statement.
```python3
try:
  var user_input = input("never say never >")
  if user_input == "never":
    raise Error("you said never")
except Error:
  print("We got an error")
```
In the example we throw our own error if the user says never

## Getting Exception messages

We can get an error message by giving the caught exception a name:
```python3
try:
  var user_input = input("never say never >")
  if user_input == "never":
    raise Error("you said never")
except Error, e:
  print("We got an error " + str(e))
```
