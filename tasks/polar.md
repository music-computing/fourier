## Background

The complex plane has two axes:
1. The $x$-axis represents the real numbers,
2. The $y$-axis stands for the imaginary.

Each DFT coefficient can be represented in this plane with the two axes for its real and imaginary parts.
That's fine, though we are typically interested in the coefficient's
**magnitude** (or 'absolute') value, and its **phase**.

These can be calculated as follows:
1. the magnitude is the distance from the origin, 
    calculated using the Pythagoras theorum as the hypotenuse of the triangle connecting the 
    origin, the position in the plane, and either axis:
    $\sqrt{real^2 + complex^2}$.
2. the phase is given by the angle (in radians) of that line from the x-axis.

The "polar coordinates" of the coefficient encode this magnitude-phase pair.


## Task

- Type: Implement
- Task: Write a function to convert DFT to polar.
- Hint: Useful libraries include cmath (`cmath.polar()`) or numpy (`np.ads` and `np.phase`).
- Bonus: Do it from scratch without those libraries!
- Bonus: Produce a polar plot of a single complex number on the complex plane using `plt.polar`.
- Reference: `polar.{dft_to_polar_with_cmath | dft_to_polar_with_numpy | one_cartesian_to_polar}` 
