# Lesson 12

## Modules

Modules are a handy way to increase functionality of a program, by giving it
access to things already written by others.
Rather than use modules, it's possible to write all of the
modules contents ourself.
We don't do this because it's quicker and easier to use modules,
and good modules have fewer bugs than programs we would write
ourselves at this stage - so why reinvent the wheel?

> We won't cover creating our own modules, since that's best
> learnt after understanding object oriented programming.
> But we will go over using them, since it'll make programming
> much easier.

## Importing Modules

We can get access to modules available to us by importing them,
we can import any of pythons standard modules this way (we can
import 3rd party modules by downloading them first).
```python3
import sys
```

If we don't need the full module we can get specific parts of
it.
```python3
from sys import builtin_module_names
```

We can choose the name we use to access a single module, or
specific part.
```python3
from sys import builtin_module_names as modules
```

Even though it's not advised, we can import all the functions
and variables from the module, without importing the module
itself, allowing us to access everything from the module
directly.
```python3
from Sys import *
```
> If a variable in the module happens to have the same name as
> a variable you have made there may be unexpected consequences
> if we import everything from a module this problem is more
> likely because it's unlikely we know everything inside the
> module or plan to use it.

## Using Modules

We can use functions and variables belonging to the module
by using the same dot style syntax as we did for working with
arrays, so: `sys.builtin_module_names` or
`cmath.sqrt(-1)`. If we imported specific
things directly from the function, then we can access them
directly.

## Modules with Python

Some useful modules in python are random, time, and sys,
among many more.
So let's see modules in action:
```python3
import sys
from time import strftime

print("date and time: " + strftime("%c"))
print("you are running: " + sys.platform)
```

We can see how this is much easier than trying to write this
functionality from scratch.

## Documentation

We can make things much easier for us using modules, however
to know how to use the modules we import, we need to look at the module's
documentation. Modules ofthen have documentation on the internet, common
places to find it are GitHub, PIP and the official python
documentation (we can also try to look for tutorials or videos for popular
modules). If the module is a standard one such as **time** or **sys**
then we can find documentation on the
[official python website](https://pip.pypa.io/en/stable/), if a module has been
installed from somewhere else then we can usually find the documentation with
the source (or at least a link to the documentation).

## PIP

PIP is a package management system that is recomended by python, we use PIP to
install modules or groups of modules which come in packages, if you have
python installed on your machine then using PIP is a good idea.
REPL can install 3rd party modules with the _libraries_ button (cube looking
button) in the top right of the editor.

---
Example - eulers_formula.py
Example - stopwatch.py
Exercise - guess_my_number.py
---
**[Example09 - eulers_formula.py](../examples/eulers_formula.py)**  
**[Exercise12 - stopwatch.py](../exercises/stopwatch.py)**  

---
**[previous lesson](./Lesson11.md)**  
**[next lesson](./Lesson13.md)**
