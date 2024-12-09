# Advent of code 2024 - Day 08: Resonant Collinearity

## Part 1

The antennas are stored in a dict (key: antenna frequency, val: list of tuple of coordinates).
From there, the antinode locations are given by: for two points A and B, the nodes are A + (A - B) and B + (B - A).

## Part 2

Weird wording, the "regardless of distance" confused me wrt the examples below. Part 1 could also be ambiguous but it explicitely says "one on either side".
I think that the input is made such that no antinode can be on non-integer multiples of the distance between antennas (ie, those fall in-between grid cells).
Still, simple change from part one by adding all `* k` antinodes past the first two.
