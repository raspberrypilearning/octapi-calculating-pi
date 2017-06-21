# Programming challenge
Write a Python program to calculate the value of π using Viète's product series.


--- hints ---
--- hint ---

To calculate a square root using Python, you will need the `math` module. Here is the code you will need to calculate the square root of 2:

```Python
import math

math.sqrt(2)
```

--- /hint ---
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
