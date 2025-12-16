# Advent of code 2025 - Day 04: Printing Department

https://adventofcode.com/2025/day/4

## Part 1

A simple convolution does the trick, counting neighbors with `[[1,1,1],[1,0,1],[1,1,1]]` as a kernel.
Then, rolls (`grid > 0`) with few enough neighbors (`neighbours < 4`) are counted by summation.

I cheated using SciPy's convolve2d function :) would be curious a write an efficient numpy on at some point.

## Part 2

It boils down to repeating part1 until convergence, suming the number of removed rolls at each iteration.

I am curious to give a try at finding a better solution, when there is time.
