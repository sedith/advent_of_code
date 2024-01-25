# Advent of code 2023 - Day 3: Gear Ratios

## Part 1

The algorithm is quite straightforward.
Scanning the rows one by one, successive digits are aggregated together until a non-digit cell is found.
For each digit, the neighbors are scanned for finding parts.
If at least one part is found while scanning the digits, then the number is labelled as part number and accumulated in the resulting sum.

## Part 2

This is essentially identical. The array is scanned and gear numbers are associated to the corresponding gear using a dictionnary (whose keys are each gear (i,j) coordinates, and values are all the neighboring numbers.)
Finally, gears with exactly 2 gear numbers are valid gears, and their gear ratio is computed and aggregated into a sum.
