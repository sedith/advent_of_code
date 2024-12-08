# Advent of code 2024 - Day 06: Guard Gallivant

## Part 1

Simple impletation based on the grid/idx/dir implemented for *2024/04*.
Increment the guard position until they leave the map.

## Part 2

The concept is to explore a branch by adding an obstacle in front of the guard at each step, and check if this leads to a loop.
There are several edge cases:
* check that the obstacle can be placed in front of the guard
    * we cannot place the obstacle on the current guard position
    * we cannot place the obstacle on the previously walked path of the guard (imply the previous)
* don't account for obstacles several times in the same location
* consider collisions with the new obstacle as well (duh)

Implementation of path as a dict whose key is the position and value is the list of directions the cell was crossed with.
The virtual path exploration also creates its own path dict.
