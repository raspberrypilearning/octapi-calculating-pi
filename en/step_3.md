## Why is calculating π difficult?

π is an **irrational number**. An irrational number is a number that cannot be written as a simple fraction, because its decimal part is infinitely long and does not repeat.

Many people think that the value of π can be calculated by dividing `22/7`. However, this only creates an approximate value: π is an irrational number, so by definition it cannot be expressed as a ratio. `22/7` also has no mathematical basis in the geometry of circles — it is merely an attempt to represent the true value of π using memorable integers.

**Do you know any other irrational numbers?**

--- collapse ---
---
title: Answer
---
There are lots of irrational numbers — two of the most commonly encountered ones are:
- `√2 = 1.4142135623730950488...`, the first number to be confirmed as irrational
- Euler's number e, the base value used in natural logarithms `e = 2.71828182845904523536028747135266249775724709369995...`

--- /collapse ---

The first formal method for calculating π was devised by Archimedes of Syracuse (287–212 BCE) around 250 BCE. It worked by fitting a circle between two polygons and estimating the circumference of the circle using the perimeters of the polygons: the circumference (c) of the circle must be greater than the perimeter of the inner polygon, and smaller than that of the outer polygon.

![π can be estimated by computing the perimeters of circumscribed and inscribed polygons](images/archimedes-pi.png)

*By Leszek Krupinski, [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/) via Wikimedia Commons*

We know the diameter (d) of the circle, and we can approximate c using the polygons. We also know that `c = π * d`. Therefore, we can estimate the value of π by rearranging the formula to `π = c/d`.

This method, or variants of it, was used by mathematicians over several centuries, with astronomer Christop Grienberger for example calculating 38 decimal places in 1630 AD.
