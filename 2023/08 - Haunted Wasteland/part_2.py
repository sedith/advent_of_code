import numpy as np
import time


class Map:
    def __init__(self, instructions):
        self.steps = []
        self.states = []
        self.nodes = {}
        for ins in instructions:
            if ins[0:3].endswith('A'):
                self.states.append(ins[0:3])
            self.nodes[ins[0:3]] = {'L': ins[7:10], 'R': ins[12:15]}


    def move(self, dir):
        self.states = [self.nodes[s][dir] for s in self.states if not s.endswith('Z')]


    def is_finished(self):
        return not len(self.states)


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        map_sheets = f.read().splitlines()

    directions = list(map_sheets[0])
    map = Map(map_sheets[2:])

    ## get number of finished steps for each starting node
    i = 0
    nb_steps = 0
    while not map.is_finished():
        map.move(directions[i])
        nb_steps += 1
        for s in map.states:
            if s.endswith('Z'):
                map.steps.append(nb_steps)
        if (i := i+1) == len(directions): i = 0

    ## compute least common multiple
    nb_steps_lcm = np.lcm.reduce(map.steps)

    toc = time.time()
    print('number of steps to reach all XXZ nodes:', nb_steps_lcm)
    print('time:', toc-tic)
