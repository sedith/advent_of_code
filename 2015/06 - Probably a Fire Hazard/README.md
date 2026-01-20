# Advent of code 2015 - Day 06: Probably a Fire Hazard

https://adventofcode.com/2015/day/6

## Part 1

Easy enough with Numpy: on a boolean array, select the rectangle corresponding to each line, and apply `+1`, `*0` or `^1` depending on the operation.
Then, return the `count_nonzero`.

## Part 2

Same as Part 1 but with `+1`, `-1` or `+2` on an integer array (and return the `sum`).
