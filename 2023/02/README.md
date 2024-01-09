# Advent of code 2023 - 02

## Part 1

Simple parsing of the input file and compare the game values to the colors in the bag (12 reds, 13 greens, 14 blues).
If any in color gets more in the game than available in the bag, it's invalid.
Sum valid IDs as it goes.

## Part 2

For each game, the fewest number of cubes of each color is the highest value of that color in all sets.
Compute as it goes and sum game powers.
