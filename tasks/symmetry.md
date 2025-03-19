## Background

One common purpose of Fourier transforms is
to isolate features of interest in the data.
This will involve:
1. either focusing on a _specific coefficient_ (one value of $k$)
2. or considering the _magnitudes_ of coefficients in isolation (ignoring the phases).

In the latter case (2.), we speak of the _spectrum_ of an input vector
(such as a pitch-class or beat-class set)
as the vector of magnitudes, $(|x_0|, |x_1|, \dots, |x_{n-1}|)$.


## Symmetry and redundancy

We can generally ignore half of those coefficients,
because the zeroth coefficient gives the cardinality of the set ...

$$
\hat{x}_0 = \sum_{j=0}^{n-1} x_j ,
$$

... and the rest of the coefficients have an 'aliasing' symmetry.

$$
\hat{x}_{n-a} = \overline{\hat{x}}_a 
$$

## Task

- Type: Implement
- Task:
  - Take any profile, such as the binary PCP vector for (the scale of) C major `[1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1]`.
  - Plot this vector as a line graph.
  - Compute DFT and plot the _spectra_ as a new line graph. Note the symmetry features described in the main text.
- Bonus: Add a Boolean argument to show/hide the symmetrically equivalent parts.
  - Hint: index from position 1 to $N/2$.
- Reference implementations:
  - `plot_spectra.compute_and_plot(hide_symmetry = True)`.
  - `equivalence.equivalence_comparison(input_list, operation = "mirror")`.
