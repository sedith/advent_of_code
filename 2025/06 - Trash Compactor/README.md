# Advent of code 2025 - Day 06: Trash Compactor

https://adventofcode.com/2025/day/6

## Part 1

Split and transpose the string to get a single tuple for each operation.

## Part 2

Here, I first transpose the string to get each operand on a single tuple.

From here, using a for loop its easy to append operands until an operator is met (non-empty last char in tuple). There is an `if` to handle empty lines separating the operations.

I... also spent an unhealthy amount of time one-lining it.  
The idea is to use `groupeby` to split the list of tuples into groups for each operation (which are separated by `(' ', ' ', ' ', ' ')`).
From here, it takes some string masturbation to get a tuple `(op1, op2, ..., operator)` for each, then performing operations and summing.  
Its unlegible and slower, so overall a good time investment.
