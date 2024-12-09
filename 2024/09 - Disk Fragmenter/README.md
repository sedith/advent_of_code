# Advent of code 2024 - Day 09: Disk Fragmenter

## Part 1

The algorithm is essentially 2 parts:
* Build the block list from the diskmap. This is achieved by incrementing the file_idx and alternating a bool for file / empty.
* Defragment the blocks. Read the list from each sides and move indexes in empty slots. This is achieved in a `do-while` (so with an ugly `break` because Python).

## Part 2

Modification of the defrag function:
1. go through the block list and locate free slots, storing slot idx and size in two co-lists
1. go through all blocks again, backward, and move each block once to the earliest position which fits, if any.
Careful to:
    * modify the `free_idx` and `free_size` lists if the
    * move each block once at most (I check that the parsed file block `b` is smaller than the one of the last moved block `idx`).
    * don't move a block later than its initial spot

Runs in ~2s. Reduced time by half by removing the fully filled slots from the free slot lists.
Could be optimized further, eg by building the two co-lists directly from the diskmap and dropping the empty blocks `'.'`.
Memoization could also work.
But mostly one should go away from the straightforward data structure (list of blocks) for some tree-based structure.
