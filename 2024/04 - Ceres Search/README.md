# Advent of code 2024 - Day 04: Ceres Search

## Part 1

Mostly a naive algorithm for pattern matching in the grid.
It scans the grid until a 'X' is found. Then, it looks over the 8-neighbors to find a 'M', and for each match it looks further in the corresponding direction to check for the full word matches.
It could probably be marginally optimized by checking the match each time any letter of 'XMAS' is encountered, and using a memoization of some sort to avoid rechecking previously seen cells.
This would likely help scaling up to larger grids.

Implementation-wise, it's nothing too fancy. The `Idx` augmented tuple handles edge-cases for the 8-neighbors look-up and the `+` is overloaded to conveniently work with the `Dir` enum.
I thus discovered that tuples (because immutable) must be overloaded through the `__new__` class function.

## Part 2

Very similar as part 1.
Intead of looking for 'X', the loop hooks on 'A's, and checks the 4 diagonal neighbors for the correct conditions.
