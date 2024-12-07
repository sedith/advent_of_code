# Advent of code 2024 - Day 05: Print Queue

## Part 1

The rules `a|b` are stored as `dict[a] = [b]`, assigning a list of latters to each former in the pairs.
Then, each update is parsed: if a `b` has a `a` in the update but placed afterward, it is flaged invalid and accounted for.
The rule dict is a `defaultdict`, which assigns a default value (according to the considered type) to new keys, to avoid try/catching KeyErrors.

## Part 2

Works similarly: when a mismatch is found, the pages are inverted, and the check resumes from the same position.
This way, the fixed update is correct up to the i-th index, and the subsequent mistaches are corrected in the `[i:]` sublist.
Fixed updates are flaged and the middle value are accounted for.
