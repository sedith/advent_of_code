# Advent of code 2025 - Day 08: Playground

https://adventofcode.com/2025/day/8

## Part 1

Not so happy with my implementation so far!
There are two parts to the puzzle: getting the closest N pairs of points, then clustering them one by one.

I think the proper way of solving the pair-sorting efficiently is with k-d tree. Currently, I'm doing partial sort (using `heapq`) using squared distance as sorting criteria (careful to avoid pair duplicates and self-pairs).

The clustering is done a bit dirty, by scanning all circuits, adding each matching one to a new set, removing matching ones from the list of circuits, then adding the new set to the list of circuits. Brrr.  
Should probably be cleaned, eg by storing the list of clustered pair for each point in a dict.

## Part 2

Same as before, but full sort instead of partial and there is an exit condition in the for loop when there is a single circuit which has lenght equal to the number of points.
