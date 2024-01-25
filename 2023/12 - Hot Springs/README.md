# Advent of code 2023 - Day 12: Hot Springs

## Part 1

Just for the sake of it, this is the brute force solution.
Just compute all possibilities given the `?` (in a bits increment fashion), and check for each if it meets the conditions.
This is obviously not scalable (~10s on my laptop).

## Part 2

I first tried to implemented a recursive algorithm to count the amount of valid combinations for each line in the inputs.
There is a global terminaison condition to the recursion (all springs have been parsed).
However, early killed are performed when blocks of '#'s break the conditions (block too large or too many blocks).
It works well for the "folded" case (i.e., Part 1). However, it does not scale well in the unfolded case.

Looking closer the recursion, the same subproblem is solved several times. This is fixed by implementing a descending dynamic programming.
Considering the state as a tuple `(idx_spring, idx_cond, size_block)`, intermediate results (i.e., the leaf of each branch of the recursion tree) are stored in a memoization dictionary, which is queried at each recursive call to avoid exploring the same branch again.
