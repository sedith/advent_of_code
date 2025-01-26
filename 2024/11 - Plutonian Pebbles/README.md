# Advent of code 2024 - Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11

## Part 1

Straigthforward implementation. Tested both with recursion and for-loop.
After doing part 2, I updated this one with memoization too. From ~250ms to ~8ms.
Using `functools.cache` makes it even faster than my custom memoization with dict (down to ~3ms).

## Part 2

Essentially building upon the recursion with memoization.

It's implemented naively, that is, the memoization dict looks like:
`{ stone number : { depth at which it is encountered : nb of leaves at depth == 0} }`
This seems suboptimal to me. Ideallly, one would store the list of leaves for each given depth below the current leaf, eg
`{ stone number : { depth below current : list of leaves } }`.
The main difference is that if a given stone is encountered at depth `N` and was previously encountered at depth `M > N`, it is not needed to explore the whole tree again but simply expand from the deepest known list of leaves.
Not implemented for now because recursions fuck up my brain.

Another solution I've seen on the subreddit is to account for multiplicity of the stones.
Instead of using a list, use a dict `{stone value: number of occurance}`. The dict gets recreated at each iteration, such that each occurance of the value at a given depth is processed only once, and its multiplicity is propagated to the next depth.
Runs slightly faster than this method, but may be less efficient than the improved memoization proposed above.
