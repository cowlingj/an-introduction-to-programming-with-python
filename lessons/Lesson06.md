# Lesson 6

## Multiple Conditional Statements in a Single Condition
We can use the word **and** as well as **or** to combine as many conditions,
like so:
```python3
duck_says = "quack"
cow_says = "moo"
if duck_says == "quack" and cow_says == "moo":
  print("all is well on the farm")
  print("here's the duck sound " + duck_says)
  print("and here's the cow sound" + cow_says)

print("condition finished")
```

### and
Both operands of **and** must be True for the **and** operation to be True.

Operators?

Yes - the conditions either side of **and** are first evaluated and then the
results of both conditions are passed to **and**, it is just as valid for these
operands to be variables, and perfectly okay to use and outside of an if
statement.
```python3
i_am_rich = False
i_can_code = True

i_should_be_a_programmer = ! i_am_rich and i_can_code
```
In the above example we use **and** with the following operand `! i_am_rich`
as well as `i_can_code` to give us a boolean `i_should_be_a_programmer` - no
suprises that `i_should_be_a_programmer == True`!

### or
Either operand of **or** must be True for an **or** to be True, **or**
operations also give us True if both operands are True.
```python3
there_are_puppies = False
there_is_code = True
there_is_coffee = True

if there_are_puppies or (there_is_code and there_is_coffee):
  print("i am happy")
```
> did you notice in the example we needed to use brackets thats because we want
> the **and** part to be done (or evaluated) first. **and** and **or** have the
> same **operator presidense** so there is no prefrence to which one gets
> evaluated first, when this is the case, statements are evaluate left to right.
> brackets "()" have a much higher operator presidense so a statement in
> brackets is always executed first.

## Multiple Conditions

We can do things if a condition is not met, including testing for more
conditions, we can do this using **else** and **elif** (short for else if).
Let's see else in action.
```python3
parents_are_looking = False
BANANA_ID = 1
CHOCOLATE_ID = 2

if parents_are_looking:
  my_food = BANANA_ID
else
  my_food = CHOCOLATE_ID
```
> Watch for the indents!

In the example we set the variable `my_food` to either `BANANA_ID` or
`CHOCOLATE_ID` depending on if the condition of `parents_are_looking` is True or
not; it may be tempting to think that this can be done without the else part,
but the else part will only execute if the condition is **not** met so if
`parents_are_looking = True`, then the body of the else will not execute.

As far as **elif** goes, it's quite similar to else but with another condition,
so the first condition in the statement (the if part) must be false, and the
condition for the **elif** must be true for the body of the **elif** part to
execute.
```python3
weather = "overcast"

if weather == "sunny":
  print("i'm going to need sunscreen")
eliif weather == "cloudy" or weather == "overcast":
  print("where did the sun go")
elif weather == "rain":
  print("raindrops keep falling on my head")
elif weather == "snow":
  print("I think I will stay inside")
else
  print("I don't know what the weather is")
```
> many **elif** statements catch many specific statements, the **else**
> statement is a catch all at the end.

In this example we look at the weather string and we act upon it in different
ways depending on its value, doing diffent things if it happens to be "sunny"
or "rain".

> Be aware that **else** and **elif** can't exist without an **if** statement
> just before them, it wouldn't make sense if they could, however **else** and
> **elif** are perfectly fine without one another.

## Nesting Conditions

The body of a conditional statement can include another conditional statement,
doing this is a teqnique called nesting.

> As a general rule of thumb, the less things are nested the better, because
> many nested statements can become confusing to think about when reading code,
> so use **elif** instead of nesting when ever possible.

When we nest statements we put the whole second statement inside the body of the
first, so the second statement is only looked at depending on the result of the
first.

> When nesting statements, especially multiple levels deep, it is often easier
> to read when the body of the second statement is in the **else** of the first.

---
**[Example004 - weather.py](../examples/weather.py)**  
**[Example005 - xor.py](../examples/xor.py)**  
**[Exercise006 - birthday_greeter.py](../exercises/birthday_greeter.py)**  

---
**[previous lesson](./Lesson05.md)**  
**[next lesson](./Lesson07.md)**  
