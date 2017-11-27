# Calculates the value of Pi using Francois Viete's infinite product series of 1593
# This program uses the Decimal module in order to increase precision
# We compare with the recipe included in the Python 3 manual demonstrating use of 
# the Decimal() module
 
# All original code: Crown Copyright 2017 

from argparse import * 
from decimal import *

# The first 100 digits (rounded up) of Pi are...
first100 = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068"

# This is the method included in the Python 3 manual as an example 
# recipe for the Decimal() module
def my_pi():
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision


# main loop
parser = ArgumentParser()
parser.add_argument("no_of_iterations", type=int, help="number of iterations")
args = parser.parse_args()

no_of_iterations = args.no_of_iterations

getcontext().prec = 100  # override standard precision
getcontext().prec += 2  # add extra digits for intermediate steps 
v, pv, n, d = 1, 0, 1, 1

for i in range(no_of_iterations):
    v = Decimal(2 + pv).sqrt()
    pv = v

    n = n * v    # numerator
    d = d * 2    # denominator

# 2.0 / viete_pi = n / d, so...
viete_pi = 2 / (n / d)

getcontext().prec -= 2
    
print("Viete estimate   = %s" % (+viete_pi))
print("Recipe estimate  = %s" % my_pi())
print("First 100 digits =", first100)
