# Advent of code 2024 - Day 09: Disk Fragmenter

## Part 1

The algorithm is essentially 2 parts:
* Build the block list from the diskmap. This is achieved by incrementing the file_idx and alternating a bool for file / empty.
* Defragment the blocks. Read the list from each sides and move indexes in empty slots. This is achieved in a `do-while` (so with an ugly `break` because Python).

## Part 2
