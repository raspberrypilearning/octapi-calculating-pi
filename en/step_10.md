# "Challenge: optimising the dartboard method"

The code you have written passes a random seed to each job, so the **entropy** on the client is distributed for use on the servers. Doing it this way allows us to implement better entropy on the client in order to improve the accuracy of the computation. However, we can make best use of the **entropy** that we have by finding the best combination of job length and number of jobs.

Run the 'dartboard' program you have written lots of times with different combinations of job size and job length and record the value of π obtained in a table like the following:

|                |     | Length of job |      |
| ---------------| --- | -----------   | ---- |
| No. of jobs    | 100 |        1000   | 5000 |
| 100            |     |               |      |
| 1000           |     |               |      |
| 5000           |     |               |      |


What was the best combination of job length and number of jobs?

### Test your understanding
Why does the accuracy seem to improve for some combinations of number of jobs and job length compared to others?

--- collapse ---
---
title: Answer
---

The entropy will be only be useful for a finite number of trials in each job, after a while the trials start to correlate (the suposedly random points begin to repeat in the same places on the unit square and form a pattern). When this happens, increasing the length of the job will not improve the accuracy of the result. Likewise, the entropy will only be useful for a limited number of jobs because after a while the client entropy will be exhausted and the jobs it launches will also start to correlate (each new job has a similar pattern of points to previous jobs). When this happens, further jobs won’t improve the accuracy of the answer either.

**The results obtained using a Monte Carlo technique using pseudo-random numbers will always be limited in accuracy by the amount of entropy available.**


--- /collapse ---

### What's next?

- How I wish I could calculate Pi. Try some "Pi Philology", find a sentence or paragraph where the number of letters in each word corresponds to the digits of π in the right order.
- Use your OctaPi to investigate the power of distributed computing! Why not learn about [Public Key Cryptography](http://www.raspberrypi.org/learning/octapi-public-key-cryptography) ?
- For more on the value of Pi, read: "Pi Unleashed" by Jörg Arndt and Christoph Haenel, Springer-Verlag, 2006, ISBN 978-3-540-66572-4. English translation by Catriona and David Lischka
