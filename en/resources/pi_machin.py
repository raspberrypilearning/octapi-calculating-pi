# Calculates the value of Pi using John Machin's arctan() formula of 1706
# Machin's formula is: pi/4 = 4* arctan(1/5) - arctan(1/239)
# The arctan() is implemented using an infinite series
# This program uses the Decimal module in order to increase precision
# We include an implementation by Nick Craig-Wood that uses fixed point
# arithmetic 
# We compare with the recipe included in the Python 3 manual demonstrating use of 
# the Decimal() module
 
# All original code: Crown Copyright 2017 

from decimal import *

# The first 100 digits (rounded up) of Pi are...
first100 = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068"

# This is my attempt at an arctan
def my_arctan(x, no_of_iterations):

    t, n, s, p = 0, 1, +1, Decimal(1) / Decimal(x)

    # Calculate arctan(x) using an infinite series 
    # arctan(x) = 1/x - 1/3*x**3 + 1/5*x**5 - ..., for x>=1
    x2 = p * p          # precalculate x**2
    getcontext().prec += 2  # extra digits for intermediate steps
    for i in range(no_of_iterations):

        t += s * p / n 

        s *= -1         # change the sign of the term
        n = n + 2       # numerator multiplier for term
        p = p * x2

    getcontext().prec -= 2
    return +t

def my_pi_machin(no_of_iterations):
    return 4*(4*my_arctan(5, no_of_iterations) - my_arctan(239, no_of_iterations))

    

# This is an arctan() function implemented by Nick Craig-Wood 
# for use in calculating Machin's formula
# It uses fixed point arithmetic
# Source: https://www.craig-wood.com/nick/articles/pi-machin/ 
one = 10000000000000000
def cw_arctan(x, one):
    """
    Calculate arctan(1/x)

    arctan(1/x) = 1/x - 1/3*x**3 + 1/5*x**5 - ... (x >= 1)

    This calculates it in fixed point, using the value for 'one' passed in
    """
    power = one // x            # the +/- 1/x**n part of the term
    total = power               # the total so far
    x_squared = x * x           # precalculate x**2
    divisor = 1                 # the 1,3,5,7 part of the divisor
    while 1:
        power = - power // x_squared
        divisor += 2
        delta = power // divisor
        if delta == 0:
            break
        total += delta
    return total

def cw_pi_machin(one):
    return 4*(4*cw_arctan(5, one) - cw_arctan(239, one))


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
# start by getting the number of iterations for Machin's algorithm
no_of_iterations = int( input('number of iterations = ') )

getcontext().prec = 100  # override standard precision

print("My Machin estimate   = %s" % (my_pi_machin(no_of_iterations)))
print("Craig-wood estimate  = %s" % (cw_pi_machin(one)/one))
print("Recipe estimate      = %s" % my_pi())
print("First 100 digits     =", first100)
