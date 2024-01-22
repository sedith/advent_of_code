# Advent of code 2023 - 13

## Part 1

A bit cumbursome but naive implementation:
* scan rows (resp. cols) one by one until two equal successive ones are found
* then check the rest equality for the pattern going from that point
* if its a global symmetry (i.e., it extends to one border of the pattern), add it to the sum
* otherwise, keep looking for a pattern

## Part 2

The algorithm is essentially the same except that instead of checking for full equality of rows/cols, I added a function to count the number of differences.
Then, instead of looking for global symmetries, I look for smudges (i.e., symmetries with strictly one difference).
