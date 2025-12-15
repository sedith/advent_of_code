# Advent of code 2025 - Day 03: Lobby

https://adventofcode.com/2025/day/3

## Part 1

Very naively, look for the highest digit among the N-1 first digits of the bank, then look for the highest digit in the trail starting from that index.

## Part 2

A direct generalization of the previous algorithm.  
For powering N batteries, there are N steps:
* look for the highest digit in the (N-1) first digits
* look for the highest digit in the tail starting at that index and up to (N-2)
* ... N times in total

One edge case due to python list indexing:
in `bank[:-0]` returns an empty string so `bank[cursor:-(nb_bat-1-i)]` fails when `i==nb_bat`. Solved with an if, but I wonder if there is another ("cleaner") way.
