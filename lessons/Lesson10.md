# Lesson 10

## File Handling

Python can support reading and writting to more than just the standard input and
standard output, like we have been doing so far, we are able to read and write
to files too.

## open

We can call the **open()** function to open a file, the function can take 1 or 2
arguments, the first being the file name and the second the __mode__, but more
on the mode later.
```python3
my_file = open("myFile.txt")
```
> Opening a file may result in an error if the file doesn't exist,
> more on errors in theis extra credit section

Calling **open()** with a single argument opens the file for reading, but if we
want to do other things, such as write to the file we need to use a different
mode.

| mode            | symbol |
|-----------------|--------|
| read            | r      |
| write           | w      |
| write and read  | w+     |
| append          | a      |
| append and read | a+     |

> There are also binary modes, but we won't look at those

Lets open a the same file again, but this time we want to append and read
from it:
```python3
my_appending_and_reading_file = ("myFile.txt", "a+"")
```
> If we open a file in append or read mode then it will create the file if it
> doesn't exist

## read

Reading a file in python can be done in a number of different ways, depending on
what we want; we can read the file as a big chunk of text, or as a list of
lines, or even line at a time.
```python3
file_for_reading = open("myFile.txt", "r")
all_the_text = file_for_reading.read()
```
The above method shows how to read the whole file as a big chunk of text.
It's just a simple call to the `read()` function that bellongs to the particular
file.

```python3
file_for_reading = open("myFile.txt", "r")
a_list_of_text = file_for_reading.readlines()
```
This method reads the file and splits it into a list of lines.
The `readlines()` function gies us all the lines as seperate items in a list,
rather than giving all the text in the file as a single block of text.

```python3
file_for_reading = open("myFile.txt", "r")
for line in file_for_reading:
  print(line)
```
This method prints out all lines of the file one by one using a for loop.
If we need to access each line of the file once to do something then this method
is ideal.

```python3
file_for_reading = open("myFile.txt", "r")
first_line = file_for_reading.readline()
```
Finally this reads the first line of the file.
We can combine this with other functions to allow us to read any line in the
file.

## write

Just as we have a number of options available to us for reading files, we have a
choice in how to write to them too; we can either write a big block of text, or
write a list of lines, see bellow for an example.
```python3
file_for_writting = open("myFile.txt", "w")
file_for_writting.write("Once upon a time")
```
The example writes the text to the file, if the file is in write mode (like in
the example) then writting begins from the start, overwritting any content
already there.
If we opened the file in append mode, then the text we wrote would have appeared
at the end of the file.
```python3
file_for_writting = open("myFile.txt", "w")
story_text = ["Once upon a time.", "There lived a programmer.", "The end."]
file_for_writting.writelines(lines_to_add)
```
This example writes each item in the list as a seperate line.

```python3
file_for_writting = open("myFile.txt", "a")
final_line = "this is the real end (or is it only the beginning?)"
file_for_writting.writeline(final_line)
```

## seek and tell

If we want to read from and write to more than just the start or end, or write
and read from the same place more than once, then we need to use two more
functions that belong to a file, **seek()** and **tell()**.
Seek is used to move the cursor to a particular point in the file, and tell is
used to tell us where the cursor currently is.

```python3
file_for_reading = open("myFile")
starting_position = file_for_reading.seek(0, 0)
also_starting_position = file_for_reading.seek(0)
end_position = file_for_reading.seek(0, 2)
one_after_cursor_position = seek(1, 1)
```
The example above shows how seek works it normally takes two arguments, the
offset (how many characters after a position) and where to start looking from
(0 = start, 1 = cursor's current position, 2 = end).

> The second argument defaults to 0 in this case if no other second argument
> is given

```python3
file_for_appending = open("myFile", "a")
where_cursor_is = file_for_reading.tell()
```
Here we use tell to find out where the cursor position is.

## close

A file should always be closed when it is no longer needed, this allows other
programs to access the file, and removes information that python gives to the
computer, saying that the file is in use.
This can sometimes be handled automatically, but this behavior shouldn't be
relied upon.
We can close a file with the file's **close()** function
```python3
file_to_close = open("myFile")
file_to_close.close()
```
---
**[Example NNN](../examples/register_writer.py)**  
**[Exercise NNN](../exercises/absent_children.py)**  

---
**[previous lesson](./Lesson09.md)**
**[previous lesson](./Lesson11.md)**
