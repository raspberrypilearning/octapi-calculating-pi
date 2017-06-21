# Step three - Representing decimals on a computer

Run your π approximation program using Viète's infinite product series, but this time change the loop so that it runs 100 times. You will notice that as the number of iterations goes up, the reported result gradually becomes exactly the same.

**Why do you think this is?**

--- collapse ---
---
title: Answer
---
Viète's product series relies on calculating the product of many terms. This breaks down in accuracy after a while because of the accuracy with which the results can be saved by the computer. The more iterations that are used, the greater the impact of any inaccuracies caused by rounding errors.

--- /collapse ---

To understand why this is a particular problem when calculating an **irrational number**, you need to know how decimal numbers (numbers with a fractional part) are stored in a computer. You are probably already familiar with the way positive integers are stored in binary. For example, here is the number 5 (00000101) which is created by adding the place values containing a 1 together, i.e. 4 + 1.

![Binary](images/binary-positive.png)

If we were to extend the binary place value headers to the _right_, they extend infinitely far with each new place value representing half the previous value:

![Binary fixed point](images/binary-fixed-point.png)

With a fixed point notation, there is a fixed amount of bits before and after the point. So in this example the number represented by 01110000 would be 1.75 which is derived from 1 + 1/2 + 1/4.

In Python, decimal numbers are represented using **floating point representation** - you may have heard them called "floats" - now you know the reason why! Floating point representation requires three things - a sign (+/-), a mantissa (the significant digits of the number) and an exponent (the power to which the number should be raised). The exponent allows the point to be moved around (hence why it is "floating") to accommodate storing a wide range of magnitudes of numbers, from the size of an atom to the mass of the sun!

Suppose you have 12 bits to store our floating point number in. The first of these represents the **sign**, or whether the number is positive (0) or negative (1). The next 7 digits represent the **mantissa** - these are the significant digits which make up the number. The floating point starts off between the sign and the mantissa. The final four bits might be the **exponent** which is the power to which the mantissa should be raised, or in other words how many places to move the point to the right.

![Binary floating point](images/binary-floating-point.png)

- Take the sign and the mantissa - 0.0110010
- Move the point to the right the number of places indicated by the exponent (in this case, 0011 or 3)
- The result is 0011.0010
- Calculate the binary numbers each side of the decimal point separately. 0011 = 3, and 0010 = 1/8 or 0.125. The number is 3.125.

### Test your understanding

**Write the number 33.5 in this format**

--- collapse ---
---
title: Answer
---
![Binary](images/binary-floating-point-answer.png)

- 0.1000011
- Move the point 6 places to the right
- 0100001.1
- 0100001 = 32 + 1 = 33
- .1 = 0.5
- Result: 33.5

--- /collapse ---

**Why can't you write the number 33.125 in this format using 12 bits?**

--- collapse ---
---
title: Answer
---
In the previous example we moved the floating point 6 places to the right. This meant that there was only one bit of the mantissa available to represent the fractional part of the number, so the highest precision available for the fractional part of the number was to the nearest 0.5. To represent a fractional part with greater precision would require a larger mantissa and therefore more bits to store the number in.

If you do a calculation in Python where the result has a greater degree of precision than the number of bits available to store it, the number will be approximated by rounding. This is what causes the Viète program to become more and more unreliable as there are not enough bits available to store the increasingly precise value of π.

--- /collapse ---

In Python, floating point numbers are stored in 64 bits - this is a standard double precision floating point number. The more bits you have available to store your floating point number in, the more precisely you can store the value of the number without rounding.

**How many bits would you need to store an irrational number like π?**

--- collapse ---
---
title: Answer
---
As we learnt from the definition of an **irrational number**, the decimal part is infinitely long and never repeats. We can never accurately store the value of π in a variable in Python because it would require an infinite number of bits!

As an extension task, you could use the [decimal module](https://docs.python.org/3/library/decimal.html?highlight=decimal#module-decimal) to improve the accuracy of your program. Can you achieve the 15 digits of accuracy after 25 iterations? How many terms in the series can you reach before accuracy is lost?

Take a look at our [example program](code/pi_viete.py) to see an implementation of the Viète infinite product series using Python's decimal module.

Using the decimal module largely removes this problem because it allows arbitrary precision (or more accurately, user defined integer precision) to be specified. The precision is still limited by the amount of memory available, in other words you can only specify finite precision: `getcontext().prec('x')`, where `x` is a finite integer.

--- /collapse ---
