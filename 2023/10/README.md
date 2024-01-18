# Advent of code 2023 - 10

## Part 1

The first step is to assess the the correct symbol for the starting cell.
This is done (in `get_start`) by checking the 4-neighbors cells and pruning the set of 6 possible symbols.
This is not the most elegant if-switch but works.
The `if 'X' in possibilities:` before removal is mandatory since `remove('X')` will raise an exception if `'X'` is not in the list (i.e. was already removed).

The `distances` array is initialized full of `-1` and filled as follow:
* the initial cell (start) is set to 0
* two cursors are initialized in each of the neighbor cells on the pipe line
* the distance value corresponding to the cursors is set to 1
* each cursor is moved to the next cell (i.e. the neighbor that is not assigned a distance yet)
* stop when no valid neighbor is found (both cursors are crossing)

## Part 2

The idea is to scan the map line by line (would also be applicable collumn-wise), and fill the masking array according to some occupancy switch, that is inverted once the scan crosses the pipe line.

The only tricky part is to deal with horizontal parts of the line. When the scan goes through several successive horizontal pipes, the flip of the switch depends on the first and last pipes values:
* if the scan goes through `F--J` or `L--7`, the switch happens
* otherwise (`F--7` or `L--J`), the occupancy isn't changed

The mask is first created using the algorithm from Part 1 to get the line (to discriminate main line against smaller loops or background pipes).
Then, non-line pixels are populated according to the switch value.
