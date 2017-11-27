# This computes the value of Pi using the 'dartboard' algorithm. This is
# a Monte Carlo method using many trials to estimate the area of a
# quarter circle inside a unit square.
#
# This code runs standalone on the client and allows you to compare
# runtime with the version running on OctaPi using Dispy.
#
# Reference: Arndt & Haenel, "Pi Uneashed", Springer-Verlag,
# ISBN 978-3-540-66572-4, 2006,
# English translation Catriona and David Lischka, pp. 39-41

# Dispy:
# Giridhar Pemmasani, "dispy: Distributed and parallel Computing with/for Python",
# http://dispy.sourceforge.net, 2016

# All other original code: Crown Copyright 2016, 2017

# 'compute' is the core calculation
def compute(s, n):
    import random

    inside = 0
    random.seed(s)

    # For all the points requested
    for i in range(n):
        # compute position of the point
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        result = x*x + y*y
        if (result <= 1.0):
            inside = inside + 1    # This point is inside the unit circle

    return(inside)



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
