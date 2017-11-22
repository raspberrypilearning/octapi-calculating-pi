## Monte Carlo method

Now we will try a **Monte Carlo** method for calculating π to see how this technique compares. The Monte Carlo method we will use is called the **dartboard method**:

- A quarter circle with a radius of 1 is drawn inside in a 1×1 square
- Random points are generated that fall inside the square, rather like darts thrown at a dart board
- By counting how many random points fall into the area inside the circle compared to the total number of points in the entire square, π can be estimated

![Random distribution of points in a square partitioned using a quarter circle](images/pi-30k.gif)

_By nicoguaro (Own work) [CC BY 3.0](http://creativecommons.org/licenses/by/3.0), via Wikimedia Commons_

The ratio of the number of points inside the quarter circle to the total number of points will approximately equal to `π/4`.

--- collapse ---
---
title: How did you calculate the ratio `π/4`?
---
Let `r` be the radius of the circle, which is the same as the length of a side of the square. Remember, we defined `r = 1` and the size of the square to be 1×1.

The `∝` symbol means "proportional to".

+ Points inside the square `∝ r²`, since `r²` is the area of the square
+ Points inside the quarter circle `∝ (πr²)/4`, since `(πr²)/4` is the area of the quarter circle

So the ratio of `points inside : all points` is `(πr²)/4 : r²`

We can simplify `(πr²)/4 : r²`:
+ multiply both sides by 4 — `πr² : 4r²`
+ divide both sides by r² — `π : 4`, which is `π/4`
--- /collapse ---

The larger the number of randomly generated points, the more accurate the estimate of π.

### Calculating whether a point is inside the circle

Here is how we will determine whether a randomly generated point lies inside the circle:

- We already know that the radius of the circle is `1`.
- `x` and `y` are points on the axes.
- Using Pythagoras' theorem about right-angled triangles (`a² = b² + c²`), we can show that for all points inside the circle `x² + y² < 1`

![Pythagoras](images/point-inside-circle.png)

_Adapted from original image by nicoguaro [CC BY 3.0](http://creativecommons.org/licenses/by/3.0), via Wikimedia Commons_

Let's look at the example from the image above:

- For our randomly generated point `x = 0.6` and `y = 0.4`.
- The radius of the circle is `1`.
- We need to find the distance of the example point from the axis point `x = 0, y = 0` — we'll call this the **radius `r`**.
- Pythagoras' theorem tells us that `r² = x² + y²`. Plug the values of `x` and `y` into the equation:

`r² = 0.6² + 0.4² = 0.36 + 0.16 = 0.52`

- To get the value of `r`, we would normally need to take the square root of the result of the equation. However, we know the circle we are comparing against has a radius of `1`. So the circle's `r² = 1² = 1`. Therefore, we can just skip taking the square root of our result altogether. 
- If the result is less than `1`, the point is inside the circle. If it is `1` or greater, the point is outside the circle.

**Calculate whether `x=0.81, y=0.62` is inside the circle**

--- collapse ---
---
title: Answer
---
- `r² = 0.81² + 0.62² = 0.6561 + 0.3844 = 1.0405`
Our condition for being inside the circle was `x² + y² < 1`. Therefore, this point is not inside the circle.
--- /collapse ---

Next, we will implement this Monte Carlo method to estimate the value of π on a computer. This will involve writing a program to generate lots of random coordinate points `x, y`, with values between `0.0` and `1.0` for both `x` and `y`.

The program will generate sets of points to test — each set is called a **trial**. We will look at how the number of points in each trial and the number of trials affects the estimated value of π.
