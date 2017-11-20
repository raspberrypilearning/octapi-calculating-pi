## Viète's method

In the 16th and 17th centuries, **infinite series methods** revolutionised the calculation of π. An infinite series method involves an infinitely long series of calculations which progressively generate a more and more accurate approximation of π. The first series discovered in Europe was an infinite product series and was found by French mathematician François Viète in 1593. It achieved 15 digits after only 25 terms.

  ![François Viète product series](images/viete-product-series.png)

This might look like a complicated equation, so let's break it down. Once you break it down into smaller parts, it becomes much easier to understand, and you'll be able to work out how you can calculate it using a computer program.

+ Open IDLE and create a new Python file.

    [[[rpi-gui-idle-opening]]]

Each **term** in the infinite series looks a bit like what you see below. You might have noticed that we need to do a calculation involving a square root (marked in purple) and then divide the result by two every time.

![First term in viete](images/first-viete.png)

+ Create a variable called `purple` to represent the square root part of the calculation, and set its value to the square root of 2.

--- hints ---
--- hint ---
To find the square root of a number in Python you will need to import the `math` library at the start of your program:

```python
import math
```
--- /hint ---
--- hint ---
You can find the square root of a number using `math.sqrt()`. For example, here is code which will calculate the square root of 16:

```python
math.sqrt(16)
```
--- /hint ---

--- /hints ---

+ Create another variable called `answer`, and then set it to the value of the whole first term in the sequence — this will be the `purple` variable divided by 2.

You can check your code at this point by adding in a line to print the value of `answer` and checking that it equals `√2/2` or `0.7071067811865476`.

So far we have calculated the value of the first term of the infinite series. However, this will not be a very precise approximation of π. The more **iterations** of the series we perform, the more accurate the result becomes. Here are the first two terms in the infinite series:

![Viete sequence highlighted in purple](images/viete-purple.png)

The dot between the two terms just means **multiply**. So to get a more accurate result we need to follow these steps:

- Calculate the value of the new `purple` section (in this case `√(2+√2)` )
- Divide this by `2`
- Multiply this result by the previous result

- Let's look at the `purple` section in more detail.

![Viete second term](images/viete-new-purple.png)

Have you noticed that the part circled in red (`√2`) is our previous purple calculation? To find the result of the new `purple` calculation, we can do this:

```python
new purple = square root of ( 2 + old purple )
```

If you look at the next term of the sequence, you will see that this rule holds true: as long as we save the result of the `purple` calculation to use next time, we can keep calculating like this on a loop, as many times as we like.

![Viete sequence highlighted in purple](images/viete-product-series.png)

+ Create a loop which runs the steps to calculate the new and more precise answer 25 times, each time saving the value of the `purple` calculation and the overall answer.

[[[generic-python-for-loop]]]

Notice that the end result of this calculation is equal to `2 / π`, but we want to know just the value of π.

+ Rearrange the equation to find out how to obtain the value of π.

```python
2 / π = result
```

### Challenge: implement Viète's method

Working through the steps described above, write a Python program to calculate the value of π using Viète's product series.

--- hints ---
--- hint ---
Here is some pseudo code to help you write your program:

```
SET purple = √2
SET answer = purple/2

FOR i FROM 1 TO 25 DO
    SET purple = √ (2 + purple)
    SET answer = answer * (purple / 2)
    PRINT 2 / answer
END FOR

```

--- /hint ---
--- hint ---
Here is a solution in Python:

```Python
# Viete example
import math

purple = math.sqrt(2)
answer = purple/2

for i in range(25):
    purple = math.sqrt(2+purple)
    answer = answer * (purple / 2)

    print("Pi = " + str(2/answer) )

```
--- /hint ---

--- /hints ---
