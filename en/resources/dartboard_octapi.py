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
import random, decimal, dispy, socket

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



server_nodes ='192.168.1.\*'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
cluster = dispy.JobCluster(compute, ip_addr=s.getsockname()[0], nodes=server_nodes)


# Input the number of trials to run and the size of each trial
no_of_points = int( input('Number of random points to include in each trial = ') )
no_of_jobs = int( input('Number of trials to run = ') )

jobs = []
for i in range(no_of_jobs):
    # Schedule the execution of the 'compute' function on one of the OctaPi nodes
    ran_seed = random.randint(0,65535) # Define a random seed for this job

    # Create a job
    job = cluster.submit(ran_seed, no_of_points)
    job.id = i # Associate an ID to the job

    # Add this job to the list of jobs
    jobs.append(job)

total_inside = 0
for job in jobs:
    inside = job() # Waits for job to finish and returns results
    total_inside += inside

total_no_of_points = no_of_points * no_of_jobs
# Override standard precision to avoid rounding problems
decimal.getcontext().prec = 100

# Calculate the estimated value of Pi
Pi = decimal.Decimal(4 * total_inside / total_no_of_points)
print(('The value of Pi is estimated to be %s using %s points' % (+Pi, total_no_of_points) ))
