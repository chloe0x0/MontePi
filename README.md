# MontePi
Monte Carlo approximation of pi for pi day! 

There is a Python version, as well as a faster C version.

The approximation works by randomly placing points in a square of side length 2 with an inscribed circle of radius 1.

The ratio of the area of the circle and the area of the square is ~ 𝝅/4

$$\pi \approx 4*\frac{Points \ inside \ Circle}{Points \ inside \ Square}$$

## MontePi.py
```console
>python montepi.py
>>> Enter the number of points to use for the approximation: 10000
>>> 𝝅 ≈  3.1264
```
