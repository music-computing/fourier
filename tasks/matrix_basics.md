## Background

While there's very little assumed knowledge in this course,
it would be useful to make sure you're comfortable with 
basic mathematical operations on matrices.

This notebook provides a 'sandpit' for trying things out.
If you're reading this in the notebook, then the basic demos above
should be enough for our purposes.
The tasks below move this on a bit further.
Those tasks are a bit more involved, but not essential for current purposes.

## Task

- Type: Implement

- Tasks: Write functions to ...
  1. Get the `shape` (m- and n-dimensions) of any 1- or 2-D array. 
  2. 'Pad' (expand) an array to double the length and width (4x the size in total) with zeros to the right and below.
  3. Reduce an array to half the length and width (1/4 total), taking the top and left most block.
  4. Implement the dot product above for 2-D arrays from scratch.

- Reference implementations:
  1. `matrix_basics.get_m_n()`
  2. `matrix_basics.pad_2x2()`
  3. `matrix_basics.back_to_half()` (this complements `pad_2x2`)
  4. Locally `matrix_basics.dot_from_scratch()`, as well as in `numpy`:
     - `np.dot(a, b)`, `np.matmul(a, b)` and `a @ b` (where a and b are np.arrays)
     - Bonus: check your work with `np.allclose`.