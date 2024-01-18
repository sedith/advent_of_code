# Advent of code 2023 - 04

## Part 1

Scratching the cards is made in the most straightforward fashion:
* split the string in two lists ('winning numbers' and 'your number')
* for each of your number, count the ones which are winning ones
* compute the value as `2**(nb_win-1)`, making sure to avoid having `**(-1)` if `nb_win == 0`.

## Part 2

Similar idea but instead of parsing cards one by one in a naive way, a dictionnary of data is first create.
To each card id is associated: (winning cards, your cards, nb of copies)
Then, cards are processed by increasing ids and duplications are handled by incrementing the 'nb of copies' of next cards.
