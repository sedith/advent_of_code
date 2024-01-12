# Advent of code 2023 - 07

## Part 1

The idea is to assign a unique id to each hand, such that ordering hands is equivalent to order ids.
The value of each card is encoded as an hexadecimal "digit", that is 2 to 9 for cards 2 to 9, then A-E for 10, J, Q, K, A (resp.).
Therefore each hand is encoded as an hexa number between `0x22222 = 0d139810 ` and `0xEEEEE = 0d978670`.
To make sure that low hands of higher type (eg, five-of-a-king of 2s) gets a higher ranking than high hands of low type (eg, pair of As), the hexa id is added to a radical of `1e6*type`. Uniqueness and ordering is ensured since `1e6 > 978670`.

Hand values are quite straightforward to compute with a proper `map` to convert the parsed string into an hexa string, that is then converted to decimal integer using `int(hexa_str, 16)`.
The only weird thing is that converting a list of char to a string has to be done with `join`: `string = ''.join(list_char)`.

Computing the rank of the hand is a cascade of ifs, not the most elegant but that was really the least interesting part imho.
Cards in the hand are parsed one by one, and number of same-of-a-kind are computed with `hand.count(card)`.
Some hands are 'terminal' and it's not use parsing the hand further once detected (e.g., five-of-a-king or full house) so it breaks.
Pairs and three-of-a-kind are not and call to parsing further (in order to discover potential two-pairs or full houses).
Adding a check to continue if the value is already parsed is mandatory to avoid tagging a three-of-a-kind as a full house at the second occurance of the value.

The rest is a fun play with `zip` and `sorted`.
`zip(*list)` does weird magic I don't fully understand. Here, it allows to get a tuple of `(hands, bids)` from a list `[(hand_0, bid_0), ...]`.
To sort `hands` and `bids` simultaneously as sorted `ids`, those are zipped with `ids` first, then sorted.

## Part 2

Almost the same solution as part 1.
The value of `'J'` in `HEAD_VALUES` is set to `0` for simplicity, instead of shifting all the digits up.
To not modify too much my previous solution, I first count and remove the Js from the hand, then compute the type as before.
Then, in a second step, the type is incremented according to the number of Js.
(Yes, another ugly if switch.)
