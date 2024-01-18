# Advent of code 2023 - 09

## Part 1

This is roughly a straightforward implementation of the algorithm described in the daily example.
For each line in the input file:
* create successive sequences of differences
* a regularization step is need: if a sequence of differences is a single element, the sequence at the next step is an empty list, which gets replaced by `[0]`
* find new element for each sequence, that is, sum all last elements from sequences of differences -- those can be aggregated for all input lines without passing through an intermediate variable

## Part 2

This is essentially identical to Part 1. The only difference is that an intermediate value is required before aggregating into the sum of extrapolated values.
