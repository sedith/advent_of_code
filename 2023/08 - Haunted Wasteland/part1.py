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


def main(data):
    directions = list(data[0])
    map = Map(data[2:])

    i = 0
    nb_steps = 0
    while map.state != STOP:
        map.move(directions[i])
        nb_steps += 1
        if (i := i + 1) == len(directions):
            i = 0

    return nb_steps


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
