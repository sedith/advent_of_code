# Advent of code 2024 - Day 09: Disk Fragmenter

https://adventofcode.com/2024/day/9

## Part 1

The algorithm is essentially 2 parts:
* Expand the list of blocks from the diskmap. This is achieved by assigning the file id or `-1` (empty) according to the parity of the index in the input string.
* Defragment the blocks.

I first implemented the defrag by processing the list with 2 indices (left and right), and assign the first non-empty value from the right to the first empty slot on the left. It terminates when the two indices cross, and the checksum is computed from there.

It can be observed however after the defrag, there will be no space between files. Hence, the list of blocks will be a compact chunk of all valid files ids, then a chunk of -1 at the end.
From there, the algorithm can be simplified:
1. Get the list of valid file blocks. The lenght N of this list is the number of the defragmented block list (minus the chunk of `-1`s which we don't care).
1. For each of the N first blocks, either pick its id if its valid, or the last unused valid block.
1. Compute the checksum as it goes.

## Part 2

Instead of using the list of individual blocks, I define a list of segments (files and free spaces) as `[(pos, id)]` where `pos` is the index of the first block and `id` is the file id or `-1` to denote free space.

The defrag function goes through all file segments, backward, and move each file to the earliest free space which fits, if any.
Careful to:
* move each block once at most,
* don't move a block later than its initial spot.

Just to be fancy, `id * p for p in range(pos, pos + size)` can be written as `id * size * (size + 2 * pos - 1) // 2`.
Essentially, its writting the sum of integers up to `pos + size - 1` minus the sum of integers up to `pos - 1`, developping and factorizing the polynomial.
