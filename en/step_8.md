# Step five - Implementing the 'dartboard' algorithm on a single standalone processor

This part of the resource can be done on any computer which can run Python 3, including a Raspberry Pi.

### Programming challenge
- Write a function that takes two parameters - an integer to use as a seed for the random number generator, and an integer number of points you would like to test.
- The function should generate that number of randomly chosen points and then test each one to determine whether or not it is inside the circle.
- The function should count and return the number of randomly generated points which fell inside the circle.

--- hints ---
--- hint ---
You will need to `import random` inside your function to be able to generate random numbers. You can then generate the numbers using `random.uniform()`.
--- /hint ---
--- hint ---
Here is some pseudo code for a function which randomly generates points using a fixed random seed.

```python
FUNCTION compute(seed, number_of_points)

    SET RANDOM SEED = seed
    SET inside = 0

    FOR i FROM 0 to number_of_points
        SET x = RANDOM NUMBER 0.0 TO 1.0
        SET y = RANDOM NUMBER 0.0 TO 1.0
        SET result = x*x + y*y

        IF result < 1
            SET inside = inside + 1
        END IF

    END FOR

    RETURN inside

END FUNCTION
```

--- /hint ---
--- hint ---
Here is a solution in Python
```python

def compute(s, n):
    import random

    inside = 0
    random.seed(s)

    for i in range(n)
        # compute position of the point
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        z = x*x + y*y
        if (z<=1.0)
            inside = inside + 1

    return(s, inside)
```
--- /hint ---


--- /hints ---

### Programming challenge
Write a Python program that uses this function to calculate the value of π.

- Include inputs for the user to define how many points are tested in each trial (n) and the number of trials (m)
- Call the function you wrote m times, generating a new random seed for each time you call the function
- Add up the total values found 'inside' the circle
- Then calculate π = (4 * total_inside) / (n * m).

--- collapse ---
---
title: Solution
---
You can see our finished code [here](source/pi_dartboard.py)
--- /collapse ---

--- /step ---
--- step ---
---
title: Step six - Comparing the two methods
---

How does the 'dartboard' method compare with Viète's infinite product series for accuracy and speed of execution? Why do you get a different answer each time you run the 'dartboard' technique but the same answer each time you run Viète's?

### Answer
Try runnning the 'dartboard' program with 25 jobs of 1000 trials (that's 25,000 trials in total). You should see only about 2 digits accuracy for 1000 times as many computations as Viète uses for 15 digit accuracy. You get a different answer each time because you are using random trials, so the program runs with different values each time.

**Monte Carlo methods are best suited to situations where there is no formula for calculation. The value of π has many methods for calculating so in this particular case it's usually better to chose one of these methods.** Monte Carlo methods are more suitable for situations where there are no formulae available, or they are in doubt.

The 'dartboard' algorithm allows us to study how the accuracy and run time of **Monte Carlo** methods are affected by how randomly the trials can chosen (the degree of **entropy** available).

The uniform random function is that provided by Python, and is actually only **pseudo-random**. Its purity depends very heavily on the **entropy** (or amount of "randomness") available via the operating system. The accuracy of the result from our program depends on the amount of entropy available on the client.

**How could the accuracy of the 'dartboard' algorithm be improved by increasing the amount of entropy available?**
--- collapse ---
---
title: Answer
---

[[[generic-theory-what-is-entropy]]]

--- /collapse ---
