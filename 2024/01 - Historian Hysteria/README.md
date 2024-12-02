# Advent of code 2024 - Day 01: Historian Hysteria

## Part 1

Simple one-to-one difference on the sorted lists.
The fancy part is the reading of the input file as two lists of integers, in particular the list transpose `lists = list(map(list, zip(*lists)))`

## Part 2

The naive implementation works but scales poorly (O(n^2)).
The better one relies on sorting both lists, but is O(n) (?).
It relies on iterating the second sorted list until the correct value is reached.
There is a memoization dict to cope for duplicates in the first list.
