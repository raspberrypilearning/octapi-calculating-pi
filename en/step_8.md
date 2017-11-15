## Comparing the two methods

How does the 'dartboard' method compare with Viète's infinite product series for accuracy and speed of execution? Why do you get a different answer each time you run the 'dartboard' technique but the same answer each time you run Viète's?

--- collapse ---
---
title: Answer
---

Try runnning the 'dartboard' program with 25 trials of 1000 points (that's 25,000 trials in total). You should see only about 2 digits accuracy for 1000 times as many computations as Viète uses for 15 digit accuracy. You get a different answer each time because you are using random trials, so the program runs with different values each time.

**Monte Carlo methods are best suited to situations where there is no formula for calculation.** The value of π has many methods for calculating, so in this particular case it's usually better to choose a different method. Monte Carlo methods are more suitable for situations where there are no formulae available, or the formulae are in doubt.

--- /collapse ---

The 'dartboard' algorithm allows us to study how the accuracy and run time of **Monte Carlo** methods are affected by how randomly the trials can chosen (the degree of **entropy** available).

The uniform random function is provided by Python, and is actually only **pseudo-random**. Its purity depends very heavily on the **entropy** (or amount of "randomness") available via the operating system. The accuracy of the result from our program depends on the amount of entropy available on the client.

The accuracy of the 'dartboard' algorithm could be improved by increasing the amount of entropy available.

[[[generic-theory-what-is-entropy]]]
