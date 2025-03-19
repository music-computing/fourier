## Background

We now apply Fourier methods to whole pieces: both real and fake.

## Task

- Type: Implement
- Task:
  - Retrieve metrical positions from the (locally hosted) single file from the BPSD dataset. 
    - Reference implementation: `metrical_positions.get_beethoven_example(file_name: str = 'Beethoven_Op057-01_FG58.csv')`
  - Create fake metrical positions usage. This can simply repeat a single pattern numerous times.
    - For example, take position-oriented list like `[4, 1, 2, 1, 3, 1, 2, 1]`, convert to onset times and repeat.
    - With these 15 events per measure, repeated for 40 measures, this makes for 60 event positions in total,
      of which the first four events are at measure 1, the 5th is at 1.125, ..., and the last is 40.875.
    - Reference implementation: `metrical_positions.make_fake_starts()`
  - Plot a histogram of start times for data of both types, with an argument for the bin size per measure.
    - Reference implementation: `metrical_positions.histogram_of_starts()`
