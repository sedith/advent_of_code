# Advent of code 2025 - Day 09: Movie Theater

https://adventofcode.com/2025/day/9

## Part 1

Very much the same approach as 2025/08. Just discovered that `max` can also take a key function, quite convenient here.
(Yes, the area of the largest rectangle is computed twice, but it makes the code nicer than creating a dict before looking for the max...)

## Part 2

Starts same as Part 1 with full sorting instead of `max`.

From there, the largest rectangles are iteratively checked until one is fully inside the polygon.  
This test is achived by checking if any of the rectangle edge intersects with a polygon edge.

Optimizations:
* Using [`itertools.pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise) saves more than a sec compared to manually constructing the comprehension list of successive pairs
* Using [`itertools.combinations`](https://docs.python.org/3/library/itertools.html#itertools.combinations) saves almost nothing but is more legible
* Instead of repeating this in the loop over edges, there is an intermediate step where edges are processed and stored in two lists for vertical / horizontal ones. Also, the non constant coordinates are stored in increasing order (avoiding recompute of min/max).

Edge-case example where my algorithm (should) fail (taken from [this post](https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/ntofllf)):
```
....................
.##################.
.#................#.
.#................#.
.#.....######.....#.
.#.....#....#.....#.
.#.....######.....#.
.#.......##.......#.
.#.......##.......#.
.#.......##.......#.
.#.......##.......#.
.##################.
....................
```