# Advent of code 2025 - Day 02: Gift Shop

https://adventofcode.com/2025/day/2

## Part 1

Simple solution, loop over numbers in all ranges and compare the two halves.

## Part 2

The same naive approach still works but takes > 1s.
Basically, for each number in each range, select sub-sequences and try repeating to see if it matches the number.
An ~25% up is done by checking that the len(number) % len(sequence) is 0, otherwise it is trivially rejected.

Given the huge number of numbers to test, it's actually more efficient to generate all possible "candidate invalid id" up to the largest bound in the input ranges.
I initially though of a while loop over increasing "seed" sequences until it overshoots the largest range.  
Instead I came up with a trickier generator which may not be more efficient, but satisfies my brain more.
Its made of two nested for-loops:
```python
for length in range(2, max_digits + 1):  # number of digits in candidate
        for seq_length in range(1, length // 2 + 1):  # lenght of repeated sequence
```
which allow to sample all start and end of candidate sequences.
Then, each candidate is tested against every range in the input.
Invalid ids are collected in a `set` to avoid duplicates (`2222` is `2`*4 and `22*2`) in this setup.

Surprisingly, sorting input ranges slightly improves the computation time. My guess is that this is specific to my input file.
It gives `max_int` for free so why not.