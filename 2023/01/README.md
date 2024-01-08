# Advent of code 2023 - 01

## Part 1

Not much to say, just a dummy parsing of the file and a char by char test `.isdigit()`.
`d[0]` gets assigned the first digit in the line, and `d[1]` gets overwritten by each number until line is over.
Marginal improvement would probably be to parse digits until `d[0]` is found, then parse the line backward until `d[1]` gets assigned.
`f.read().splitlines()` over `f.readlines()` allows to get read of `\n` for each lines (not useful here but will be).

## Part 2

Very inefficient solution: just replace written numbers by corresponding digit in line, before applying algo from part 1.
In order to account for overlapping written numbers (eg, `eightwo` or `oneight`), I simply keep the first and last letter of each digit when replacing.
Thus `one` becomes `o1e` and `eight` becomes `e8t`.
