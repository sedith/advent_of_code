# Advent of code 2025 - Day 11: Reactor

https://adventofcode.com/2025/day/11

## Part 1

Simple recursion with memoization.

## Part 2

Again, recursion with memoization.
I naively tried to carry the full path and check at the end if `'dac'` and `'fft'` are in it, but it obviously hangs.
Instead I carry a 2-bits code that describes if each string is seen along the path (updated with or `|`), and check if its `0b11` at the end.
