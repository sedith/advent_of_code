# Advent of code 2025 - Day 07: Laboratories

https://adventofcode.com/2025/day/7

## Part 1

Beam positions are described with a tuple `(x,y)`. The propagation methods are either normal downward propagation and splitting in two.
At each propagation step we go one line downward, and propagate each beam according to the char in the corresponding cell of the data.

The beams are stored in sets instead of lists, otherwise duplicates explode and the loop takes forever.

I initially though that the question was the number of beams on the last line, when I realized it wasn't I went for the lazyest modification for counting splits with the global variable incremented in `split_beam`.

The code assumed there is no splitting outside of the grid which can be quickly visually assessed on the input. If not, more if/else must be used.

## Part 2

Recursion with memoization for DFS, returning one when the beam reaches the bottom line.