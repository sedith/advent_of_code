import numpy as np


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


def main(data):
    directions = list(data[0])
    map = Map(data[2:])

    ## get number of finished steps for each starting node
    i = 0
    nb_steps = 0
    while not map.is_finished():
        map.move(directions[i])
        nb_steps += 1
        for s in map.states:
            if s.endswith('Z'):
                map.steps.append(nb_steps)
        if (i := i + 1) == len(directions):
            i = 0

    ## compute least common multiple
    return np.lcm.reduce(map.steps)


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example3.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
