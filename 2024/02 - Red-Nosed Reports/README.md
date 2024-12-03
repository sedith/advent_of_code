# Advent of code 2024 - Day 02: Red-Nosed Reports

## Part 1

Straightforward implementation of the level checker: go through report lines, slide a window of the levels and check safety.

## Part 2

Similar but the safety check is recursive. When an inconsistency is encountered, the check is recursively called on the two sublists by removing either bad level.
Edge case that I didn't see first: if the inconsistency is at the second pair (level 2 and 3), it is also necessary to check safety by removing level 1, even though it was consistent wrt level 2. Otherwise, it is possible that a viable solution is not checked. Doesn't apply to the next pairs since the increase/decrease direction is already constrained.
Very minor optimization: if the error is that the two levels are equal, there is only one sublist to explore.
