# Advent of code 2023 - Day 15: Lens Library

## Part 1

Implement the HASH algorithm described in text and forloop over the input.

## Part 2

Again, direct implementation of the algorithm described in text.
The data structure is rather simple:
* a list of list for boxes
* each box is a list of tuples (label, focal_length)

Finding if a label is present in the box is done with a list comprehension:
`idx = [i for i,(l,f) in enumerate(boxes[box_id]) if l == label]`
