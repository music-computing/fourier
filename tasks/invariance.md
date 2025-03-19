## Background

The DFT magnitudes (spectrum) of a set
are equivalent to that of the set's:
- rotation (any step size) (= musical `transposition'),
- mirror image (= musical `inversion'),
- complement,
- scalar multiple.


## Task

- Type: Implement
- Task:
  - Take any vector, such as the binary PCP vector for (the scale of) C major `[1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1]`. 
  - Write a function to calculate the DFT of this set and demonstrate the various equivalences mentioned above:
    1. First, make a new set by rotating the original (equivalent to musical transposition).
       - Hint: index `0:m` and `m:n` and reverse, where $1 < m < n$. 
    2. Next reverse the set. Hint: `[::-1]`. 
    3. Then, take the complement. Hint: map 0 to 1 and 1 to 0.
    4. Finally, proportionally increase the amplitudes, e.g., by replacing the 1s with 2s (double all the values). 
  - In each case, verify that the altered form returns the same absolute DFT values (again, magnitudes, not phase). 
  - Bonus: try your function on several different source sets and verify that they are _not_ equivalent to each other.
- Reference implementation: `equivalence.equivalence_comparison()` 
  - The `operation` arguments are ["rotate", "mirror", "multiply", "complement"] (note: not repeat).
