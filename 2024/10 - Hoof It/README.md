# Advent of code 2024 - Day 10: Hoof It

## Part 1

(Reusing the Dir/Pos implementation for the grid from 2024/04.)
The grid is scanned for trailheads (`0`s), and for each the trails are explored.
The data structure is a set of positions for each cells of a given altitude that are in the path.
We use sets to account for the fact that a position can be reached from several others.
The lists for levels 1-9 are created iteratively at looking at the 4-neighbors of the position at the level below.
The trail score is the number of cells at level 9.

## Part 2

Again, the grid is scanned for trailheads.
The data structure is a tree-based implementation. Each node of the tree has a list of predecessors and successors and each branch is explored one after the other.
The rating is computed by recursively exploring each branch and accounting for it if it reaches a summit (`z=9`).

This was actually an attemp at implementing something for part 1, until I realized that I completely disregarding the fact that node count be seen several times. I put this code aside, solved part 1, and realized this was exactly what I needed for part two, so I simply reworded `score` into `rating`.
