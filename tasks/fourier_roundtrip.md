## Background

The Fourier transform is used in many settings, across audio, images and more
and for many purposes including the derivation of important information
for use cases in research, data compression, and more.
 
We can observe how effectively it retains the original data by running a 'roundtrip':
use Fourier to 'encode' the data to a small representation size 
and then 'decode' it back to the original (or nearly).

A classic way to test the effectiveness of a system like this is to run a 
'roundtrip' where you compare the data you star with to what comes back from an encoding-decoding cycle. 


## Task

- Type: Implement roundtrip
- Task:
  - Import or create some synthetic data, like an 8x8 array with a continuous tone pattern.
  - Import an algorithm for the fourier transform (e.g., `import scipy.fft as fft`) 
    - (Bonus: code it from scratch)
  - Take the source data, run the fft on that source, and then the inverse fft on the fft output.
  - Compare the final data with the original.
- Reference implementation (in the notebook): `test_roundtrip()`
