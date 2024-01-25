# Advent of code 2023 - Day 8: Haunted Wasteland

## Part 1

Straightforward. Implemented the map as a class for convenience.
Start at `'AAA'``L`/`R` moves (repeat as needed) until `'ZZZ'` is reached.

## Part 2

Start simultaneously at each `'XXA'` nodes, then follow moves. For each node, count the number of necessary steps to reach a terminal state `'XXZ'`, using the algorithm from Part 1.
The smallest number of steps to terminate all states simultaneously is the Least Common Multiple of the number of steps needed to terminate each one (computed using `numpy.lcm` because I'm lazy :( )
