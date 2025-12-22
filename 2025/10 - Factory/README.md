# Advent of code 2025 - Day 10: Factory

https://adventofcode.com/2025/day/10

## Part 1

Cool problem! Took me a while to formalize it nicely.

The idea is realizing that pressing a button operates a XOR on the indicator lights (the ints of the buttons are the 1-bits of the XOR operand).
From there, XOR is commutative and only of parity of the number of press of each button matters, hence each should be pressed 0 or 1 time.  
So given a machine defined as `[target] (btn_1) (btn_2) ... (btn_n)`, finding the smallest button combination to reach the target is equivalent to solving
```
min_{x_i} sum(x_i)
st. [target] = x_1 * btn_1 ^ x_2 * btn_2 ^ ... x_n * btn_n
    x_i in {0,1}
```
where basically `x_i` are selection booleans that describe is the button is pressed or not.

This is solved efficiently with DP (since the number of bits for the integers is low), where the cost is the number of button pressed and transitions are take/not-take.

The parsing of the string into target and operands is ugly, tho.

## Part 2
