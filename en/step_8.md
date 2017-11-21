## Comparing the two methods

How does the dartboard method compare with Viète's infinite product series for accuracy and speed of execution? Why do you get a different result each time you run the dartboard technique, but the same result each time you run Viète's?

--- collapse ---
---
title: Answer
---

+ Try runnning the dartboard program with 25 trials of 1000 points (that's 25000 trials in total).

You should only see about 2-digit accuracy, even though you've performed a 1000 times more computations as the Viète method needs for 15-digit accuracy (remember you calculated 25 terms with it). Because you are using random trials, the program runs with different values each time, giving you get a different result.

**Monte Carlo methods are best suited to situations where there is no formula for calculation.** There are many methods for calculating the value of π, so in this particular case it's better to choose a non–Monte Carlo method if you want an accurate value.

--- /collapse ---

The dartboard algorithm allows us to study how the accuracy and runtime of a Monte Carlo method is affected by how randomly the trials can chosen.

The `uniform random` function provided by Python is actually only **pseudorandom**. Its purity depends very heavily on the **entropy** (or amount of "randomness") available via the operating system. Therefore, the accuracy of the result calculated by our dartboard program depends on the amount of entropy the OctaPi client machine has; if you could increase the amount of entropy, you would thereby increase the accuracy of the dartboard algorithm.

[[[generic-theory-what-is-entropy]]]
