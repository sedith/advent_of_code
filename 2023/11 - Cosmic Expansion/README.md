# Advent of code 2023 - Day 11: Cosmic Expansion

## Part 1

The first step is to expand the space map. Each "empty" lines and collumns are simply duplicated using `np.insert`.
The shortest path between two galaxies is the norm 1 distance of their `(i,j)` coordinates.
The unique pairs are scanned with two nested `for` loops, summing the distances as we go.

## Part 2

The norm 1 computation is untouched, but the way of getting the `(i,j)` coordinates needs to be revised to avoid adding millions of black lines in the space image.
Instead of the naive algorithm from Part 1, a twin map of coordinates is initialized such that `coord_map[i,j] == [i,j]`.
Then, scanning the space image row-by-row and col-by-col, the coordinates are expanded by the given factor (`1e6`) when empty spaces are encountered.
