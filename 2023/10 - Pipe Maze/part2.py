import numpy as np
import matplotlib.pyplot as plt


class PipeMap:
    def __init__(self, sketch):
        self.map = np.array([list(line) for line in sketch])
        self._moves = {
            'L': np.array([0, -1]),
            'U': np.array([-1, 0]),
            'D': np.array([1, 0]),
            'R': np.array([0, 1]),
        }  # map directions with [i,j] increments

    def get_start(self):
        ## find 'S' in map
        start = tuple(np.argwhere(self.map == 'S')[0])

        ## check 4-neighbor cells and remove possibilities accordingly
        possibilities = ['|', '-', 'L', 'J', '7', 'F']
        ## check top cell
        ij = self.move(start, 'U')
        if self.map[ij] not in ['|', '7', 'F']:
            possibilities.remove('L')
            possibilities.remove('J')
            possibilities.remove('|')
        ## check left cell
        ij = self.move(start, 'L')
        if self.map[ij] not in ['-', 'F', 'L']:
            possibilities.remove('7')
            if 'J' in possibilities:
                possibilities.remove('J')
            possibilities.remove('-')
        ## check bottom cell
        ij = self.move(start, 'D')
        if self.map[ij] not in ['|', 'L', 'J']:
            possibilities.remove('F')
            if '7' in possibilities:
                possibilities.remove('7')
            if '|' in possibilities:
                possibilities.remove('|')
        ## check right cell
        if len(possibilities) > 1:  # stop here if already solved
            ij = self.move(start, 'R')
            if self.map[ij] not in ['-', '7', 'J']:
                if 'L' in possibilities:
                    possibilities.remove('L')
                if 'F' in possibilities:
                    possibilities.remove('F')
                if '-' in possibilities:
                    possibilities.remove('-')

        ## replace char 'S' in map
        self.map[start] = possibilities[0]

        return start

    def move(self, pos, dir):
        i = max(min(pos[0] + self._moves[dir][0], self.map.shape[0] - 1), 0)
        j = max(min(pos[1] + self._moves[dir][1], self.map.shape[1] - 1), 0)
        return (i, j)

    def mark_line(self, start):
        ## init two cursors to follow the pipes in both directions
        neighbors = {  # maps pipes to directions
            '|': ('U', 'D'),
            '-': ('L', 'R'),
            'L': ('U', 'R'),
            'J': ('L', 'U'),
            '7': ('L', 'D'),
            'F': ('R', 'D'),
        }
        cursors = [self.move(start, d) for d in neighbors[self.map[start]]]
        mask = -np.ones(self.map.shape, dtype=np.int16)
        mask[start] = 1

        stop = False
        while not stop:
            for ci in range(2):
                pos = cursors[ci]
                mask[pos] = 1
                dirs = neighbors[self.map[pos]]
                invalid_neighbors = 0
                for d in dirs:
                    if mask[self.move(pos, d)] == -1:
                        cursors[ci] = self.move(pos, d)
                    else:
                        invalid_neighbors += 1
                if invalid_neighbors == 2:
                    stop = True

        return mask


def main(data):
    pipes = PipeMap(data)
    start = pipes.get_start()  # replace the S in the pipe map
    mask = pipes.mark_line(start)

    ## scan map line by line and flip the occupancy switch to fill the mask
    for i, line in enumerate(pipes.map):
        label = False  # 0 for outside, 1 for inside
        memory = None  # store the value of the pipe when entering horizontal sections
        for j, cell in enumerate(line):
            if mask[i, j] == -1:
                mask[i, j] = 2 * label
            elif cell == '|':
                label = not label
            elif cell in ['F', 'L']:
                memory = cell
            elif (memory == 'F' and cell == 'J') or (memory == 'L' and cell == '7'):
                label = not label

    plt.imshow(mask)
    plt.show()

    return np.count_nonzero(mask == 2)


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example5.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
