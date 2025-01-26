# Advent of code 2024 - Day 10: Hoof It

https://adventofcode.com/2024/day/10

## Part 1

(Using complex for grip positions again.)
The grid is scanned for trailheads (`0`s), and for each the trails are explored.
The exploration performed altitude by altitude. For each cell at a given level, the 4-neighbors of scanned and matching positions (next altitude) are stored in a set (accounting for the fact that a position can be reached in several ways).
The trail score is the number of cells at level 9.

## Part 2

Again, the grid is scanned for trailheads.
The data structure is a tree-based implementation. Each node of the tree has a list of predecessors and successors and each branch is explored one after the other.
The rating is computed by recursively exploring each branch and accounting for it if it reaches a summit (`z=9`).

The first implementation of part 2 (before switching to complex) was actually an attemp at implementing something for part 1, until I realized that I completely disregarding the fact that node count be seen several times. I put this code aside, solved part 1, and realized this was exactly what I needed for part two, so I simply reworded `score` into `rating` and it worked out of the box.
