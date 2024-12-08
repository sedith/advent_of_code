# Advent of code 2024 - Day 06: Guard Gallivant

## Part 1

Simple impletation based on the grid/idx/dir implemented for *2024/04*.
Increment the guard position until they leave the map.

## Part 2

The concept is to explore a branch by adding an obstacle in front of the guard at each step, and check if this leads to a loop.
There are several edge cases:
* check that the obstacle can be placed
    * we cannot place the obstacle on the current guard position
    * we cannot place the obstacle on the previously walked path of the guard (imply the previous)
* don't account for obstacles several times in the same location
* consider collisions with the new obstacle as well (duh)

Implementation of path as a dict whose key is the position and value is the list of directions the cell was crossed with.
The virtual path exploration also creates its own path dict.
For efficiency, the dict stores only path nodes, ie when there is a change of direction. This avoid building sparser dicts, since the explore function checks appartenance to the lists at each step.
The full path is stored in a separate list to check that the obstructions.
