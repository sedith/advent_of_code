# Advent of code 2023 - Day 16: The Floor Will Be Lava

## Part 1

The state of a ray is a tuple `(position_head, direction)` that describes its propagation.
A list of ray is maintained and they all get propagate by one cell at each step. The propagation outcome is defined by the value of the new cell hosting the head of the ray:
* empty cell: nothing happens
* mirror: change direction according to mapping defined in global dictionaries
* splitter: remove ray from list and add two new ones with proper head and directions
* border (i.e., head goes out of the map): depop ray

To energize cells only once, a 'twin' of the contraption map is maintained, whose cells are enabled at the first time a ray crosses it.
The value we are looking for is the amount of enabled cells therein.

Finally, to avoid cycles, the twin map also acts as a memory of rays passing by and their directions. Once a ray crosses a cell which has already been visited in the same direction, its propagation is stopped.

## Part 2

Doing the same propagation scheme for each starting ray and accounting for the maximum is doable, but it does not exploit memory between each new 'starting configuration'.

The key idea is to assess that cells "of interest" in the grid are splitters.
That is, once on an empty cell or a mirror, given a direction, there is one and only one splitter from which the ray comes, and one and only one splitter (or wall) in which the ray will go.

Therefore, the data that needs to be stored for efficient reusage is: given a splitter and a direction, what are all the cells that will be visited and which is the next splitter that is met, if any.
Then, the exploration algorithm stores each split of the ray in a list, and elements of the list are processed one by one until a wall or an already explored cells.
Explored paths are stored in a memoization variable to be reused between scans.

Concerning the data structure: a state is again described by a tuple (`NamedTuple` for legibility), such that they can be used as dictionary keys.
To each state is associated a list of next states (empty if it hits a wall, else the output of the next splitter depending of direction), and the list of `(i,j)` coordinates that are crossed on the way.

If the current state is in the memoization dict, the shortcut is used. Else, finding the next cell is performed in a while loop (`get_next_interesting_cell`).

The coordinates are aggregated in a large list along the full scan of the ray, then turned in a set once at the end to get rid of duplicates.
