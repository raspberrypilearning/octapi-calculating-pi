## Dartboard algorithm on a standalone processor

You can do this part of the resource on any computer able to run Python 3, including a Raspberry Pi.

### Challenge: write a function to test random points
- Write a function that takes two parameters: an integer to use as a **random seed** for the random number generator, and an integer number of points you would like to test.

[[[generic-python-random-seed]]]

- The function should generate that number of randomly chosen points and test each one to determine whether or not it falls inside the circle.
- The function should count and return the number of randomly generated points which fell inside the circle.

[[[generic-python-simple-functions]]]

--- hints ---
--- hint ---
You will need to `import random` inside your function. Then you can generate the random numbers you need using `random.uniform()`.
--- /hint ---
--- hint ---
Here is some pseudocode for a function which randomly generates points using a fixed random seed.

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
Here is a solution:
```python

def compute(s, n):
    import random

    inside = 0
    random.seed(s)

    for i in range(n)
        # compute position of the point
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        result = x*x + y*y
        if (result <= 1.0)
            inside += 1

    return(inside)
```
--- /hint ---
--- /hints ---

### Challenge: calculate π using your function
Write a Python program that uses this function to calculate the value of π.

- Include inputs to allow the user to type in how many points are tested in each trial (`N`) and the number of trials (`M`)
- Call the function you wrote `M` times, generating a new random seed for each time you call it
- Add up the total values found inside the circle
- Then calculate `π = (4 * total_inside) / (N * M)`

--- hints ---
--- hint ---
You will need to use Python's `decimal` module to make sure you don't encounter problems with the precision of numbers you are able to store.

1. Add the line `import decimal` at the start of your program
1. Set up the precision with this line of code
    ```python
    decimal.getcontext().prec = 100
    ```
1. When you calculate the estimated value of Pi, use the `Decimal` type from the `decimal` library

```python
pi = decimal.Decimal( YOUR CALCULATION HERE )
```
--- /hint ---
--- hint ---
Here is some pseudocode to help you:

**INPUT** number of points
**INPUT** number of trials
**SET** total inside = 0

**FOR** i **FROM** 0 **TO** number of trials
...**GENERATE** random seed
...**CALL** compute(seed, number of points)
...**ADD** result to total inside

**SET** total points = number of points * number of trials

**CALCULATE** 4 * total inside / total points

**PRINT** result

--- /hint ---

--- hint ---
Here is how your code might look:

```python
import random, decimal

# Input the number of trials to run and the size of each trial
no_of_points = int( input('Number of random points to include in each trial = ') )
no_of_trials = int( input('Number of trials to run = ') )

print(('Doing %s trials of %s points each' % (no_of_trials, no_of_points)))
total_inside = 0

# Run the desired number of trials
for i in range(no_of_trials):

    # Create a new random seed
    ran_seed = random.randint(0,65535)

    # Run the compute function with this seed
    inside = compute(ran_seed, no_of_points)

    # Add this number to the total of points found inside
    total_inside += inside

    # Report back every 1000 trials
    if (i % 1000 == 0):
        print(('Executed trial %i using random seed %i with result %i' % (i, ran_seed, inside)))

# Calculate the total number of points tried
total_no_of_points = no_of_points * no_of_trials

# Override standard precision to avoid rounding problems
decimal.getcontext().prec = 100

# Calculate the estimated value of Pi
Pi = decimal.Decimal(4 * total_inside / total_no_of_points)
print(('The value of Pi is estimated to be %s using %s points' % (+Pi, total_no_of_points) ))
```

You can see our complete finished code [here](resources/pi_dartboard.py).
--- /hint ---
--- /hints ---
