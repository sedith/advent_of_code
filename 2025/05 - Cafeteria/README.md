# Advent of code 2025 - Day 05: Cafeteria

https://adventofcode.com/2025/day/5

## Part 1

Naive implementation: for each ingredient, check if it belongs to any fresh id range.

## Part 2

The idea here is to store a "parsed" list of fresh id ranges.
For each range, check if it belongs to any parsed one. If so, merge them, else append to the list of parsed ranges.

There are a few edge cases to take care of, but they can be alleviated by sorting the initial list of ranges by increasing start.
