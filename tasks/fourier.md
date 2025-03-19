## Background

The Fourier equation can be expressed in a number of ways.

Perhaps the most 'standard' expression is as follows:

$$
\hat{x}_k = \sum_{j=0}^{n-1} x_j e^{-i 2 \pi k j / n}
$$

It (this) can also be decomposed in various ways,
perhaps most succinctly as
$F = Af$, where 
$f$ is a time signal,
$F$ is the discrete Fourier transform (DFT),
and $A$ is an $N$x$N$ matrix with coefficients
$$
a_{i,j} = \frac{1}{\sqrt{N}} e^{- i \frac{2\pi}{N} ij}
$$

For example, where $N=4$:
$$
    {\bf A} = \frac{1}{\sqrt{4}} \begin{pmatrix}
    1 & 1 & 1 & 1\\
    1 & -i & -1 & i\\
    1 & -1 & 1 & -1\\
    1 & i & -1 & -i
    \end{pmatrix}
$$

## Task

- Type: Implement
- Tasks:
  1. Implement a matrix DFT (of `A` above) from scratch.
     - import: only `numpy`
     - args: only `n` (`n=4` in this example).
  2. Now take your answer to part 1 of this task and modify it to take in a signal `x` of length `n` and return the DFT. 
     - Hint: use `x[i]`
  3. Finally, write a combined function that computes the DFT, including an internal step for matrix `A`. 
     - Hint: use `np.dot(x, square_dft_matrix(n))`
- Reference implementations:
  1. `fourier.square_dft_matrix()`
  2. `fourier.dft_dot_product_steps()`
  3. `fourier.dft_at_once()`
