# Advent of code 2024 - Day 07: Bridge Repair

## Part 1

Recursion on the list of possible outputs.
Termination: when the list of numbers to process is empty, return the full list
Recursion: for each possible value in the list, create 2 branches for sum and mult.

## Part 2

Mostly similar, with 3 operations. I tried minor operations, among which the branches are terminated if the current value is already bigger than the expected outcome.
Didn't manage to reduce below ~3s.
