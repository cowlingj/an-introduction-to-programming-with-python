# Lesson 3

## User Input

So how can we interact with our program while it's running?

The answer is adding user input.

## input

The input function takes whatever the user types in before pressing the return
key. A prompt can optionally be added to input to give the user a hint as to
what to type.

Let's see an example of the print function.

```python3
input("hello who are you? ")
```

> The space at the end of the prompt string seperates it from the user input
> try using input without the trailing space and notice the difference.

But there isn't much point in getting the user to input something without
assigning it a variable, if we want to use that input we need to instead write:

```python3
username = input("hello who are you?")
```

so now when we refer to `username` we are refrencing the string of text the user
entered.

---
**No examples or exercises here, onto the next lesson!**
