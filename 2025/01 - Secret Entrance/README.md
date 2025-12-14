# Advent of code 2025 - Day 01: Secret Entrance

https://adventofcode.com/2025/day/1

## Part 1

This is simply getting the mod 100 of the dial number when we hit it and counting 0s.

## Part 2

The number of time the dial passes a 0 is the difference between the "number of 100s" of a dial number and the next.  
Using this formula are 2 edge cases to handle when the dial hits exactly 0:
* when the dial hits 0 coming from the right, the last 0 isn't counted
* when the dial is at 0 and goes to the left, the starting 0 is counted while it shouldn't
