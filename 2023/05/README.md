# Advent of code 2023 - 05

## Part 1

Rather straightforward: For each seed, apply direct mapping `map: seed -> loc` and find minimum location value.
The mapping is handled through a list of list (one for each intermediate mapping).
Each intermediate mapping is a list of ranges defined by `dst`, `src`, `len`, such that
*for all `j` in `range(src, src+len)`, `mapping(src+j) = dst + j`*.

## Part 2

Instead of trying `2e9` times, it's more covenient to apply the inverse mapping `map^-1: loc -> seed` from `loc=0`, then check for validity of the location (i.e. `map^-1(loc)` is in the ranges of existing seeds).
I work in a kind of dichotomie, taking a step "quite large but not too much" (e.g. `step = 1e5`).
If `loc+step` is invalid, I keep the same step and increment (`loc += step`).
If its valid, step got divided by two and I recheck `loc+step`.

There is a priori no reason for not missing the first valid loc.
E.g., take a step of `1000`. The first two valid seed ranges afe `200 -> 500` and `1001 -> 2000`, the algo will miss the first batch.
Its working under the assumption that the mapping ranges are continuous segments (instead of sparse points), and most importantly that ranges are large enough not to miss them with a "reasonable" step.

This solution seemed pretty smart when I came out with it, tho.
