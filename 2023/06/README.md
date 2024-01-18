# Advent of code 2023 - 06

## Part 1

This is the naive brute force implementation.
The funny part is the one-liner parsing of the race sheets (line 11). This is fucking unreadable.

Then, races are processed by checking all solutions.
The loop breaks once a non-winning case if processed after winning ones for (very minor) optimization.

## Part 2

This is the proper way to go: solve the simple quadratic equation `x**2 + x*T - D = 0`, then round the solutions to get a discrete range of ways to beat the proposed time.
