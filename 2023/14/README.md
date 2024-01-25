# Advent of code 2023 - 14

## Part 1

Scan the grid line by line, and for each rock, move it up while the above cell is free.
I made a fancy Platform class to play with `__getitem__` and `__setitem__`.

## Part 2

Now we got to tilt the platform in all four cardinal directions, `1e9` times. Well we got to optimize a bit.
Instead of naively parsing row-wise and "moving rocks north" one cell by one cell (implying an extra while),
it's much more efficient to scan collumns and count the available free space until a rock is found, then move the rock by that amount.

It makes it also much easier to consider other directions (just changing the order of row/col scan).
My first implementation consisted of rotating the platform counterclockwise and tilting always north. I'm not sure which solution I find the most elegant.

Regardless of those marginal improvements, the main idea patterns will eventually converge to some repeating cycle.
Therefore the easiest is to store an ordered memory of the platforms state as we go.
As soon as a grid pattern is found that already exists in the memory buffer, we're good. Just a bit of head scratching to find the formula that yields the index of the `1e9`th iteration within this cycle.

It runs in ~1.8s on my laptop. I believe that going faster would require a smarter way of moving rocks instead of scanning the full grid. Something like maintaining an array of coordinates of rocks and walls and computing movements in an analytical manner.
