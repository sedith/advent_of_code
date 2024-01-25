import numpy as np
import time

START = 'AAA'
STOP = 'ZZZ'


class Map:
    def __init__(self, instructions):
        self.state = START
        self.nodes = {}
        for ins in instructions:
            self.nodes[ins[0:3]] = {'L': ins[7:10], 'R': ins[12:15]}

    def move(self, dir):
        self.state = self.nodes[self.state][dir]


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        map_sheets = f.read().splitlines()

    directions = list(map_sheets[0])
    map = Map(map_sheets[2:])

    i = 0
    nb_steps = 0
    while map.state != STOP:
        map.move(directions[i])
        nb_steps += 1
        if (i := i+1) == len(directions): i = 0


    toc = time.time()
    print('number of steps to ZZZ:', nb_steps)
    print('time:', toc-tic)
