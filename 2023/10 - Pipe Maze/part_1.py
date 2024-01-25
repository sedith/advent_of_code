import numpy as np
import time
import matplotlib.pyplot as plt


class PipeMap:
    def __init__(self, sketch):
        self.map = np.array([list(line) for line in map_sketch])
        self._moves = { 'L': np.array([0,-1]), 'U': np.array([-1,0]), 'D': np.array([1,0]), 'R': np.array([0,1]) }  # map directions with [i,j] increments


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
            if 'J' in possibilities: possibilities.remove('J')
            possibilities.remove('-')
        ## check bottom cell
        ij = self.move(start, 'D')
        if self.map[ij] not in ['|', 'L', 'J']:
            possibilities.remove('F')
            if '7' in possibilities: possibilities.remove('7')
            if '|' in possibilities: possibilities.remove('|')
        ## check right cell
        if len(possibilities) > 1:  # stop here if already solved
            ij = self.move(start, 'R')
            if self.map[ij] not in ['-', '7', 'J']:
                if 'L' in possibilities: possibilities.remove('L')
                if 'F' in possibilities: possibilities.remove('F')
                if '-' in possibilities: possibilities.remove('-')

        ## replace char 'S' in map
        self.map[start] = possibilities[0]

        return start


    def move(self, pos, dir):
        i = max(min(pos[0] + self._moves[dir][0], self.map.shape[0]-1), 0)
        j = max(min(pos[1] + self._moves[dir][1], self.map.shape[1]-1), 0)
        return (i,j)


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        map_sketch = f.read().splitlines()

    pipes = PipeMap(map_sketch)
    start = pipes.get_start()
    distances = - np.ones(pipes.map.shape, dtype=np.int16)  # -1 everwhere for empty pixels, to be filled for distances along the line

    ## init two cursors to follow the pipes in both directions
    neighbors = {  # maps pipes to directions
                    '|': ('U','D'),
                    '-': ('L','R'),
                    'L': ('U','R'),
                    'J': ('L','U'),
                    '7': ('L','D'),
                    'F': ('R','D'),
                }
    cursors = [pipes.move(start, d) for d in neighbors[pipes.map[start]]]
    distances[start] = 0

    i = 1
    stop = False
    while not stop:
        for ci in range(2):
            pos = cursors[ci]
            distances[pos] = i
            dirs = neighbors[pipes.map[pos]]
            invalid_neighbors = 0
            for d in dirs:
                if distances[pipes.move(pos, d)] == -1:
                    cursors[ci] = pipes.move(pos, d)
                else:
                    invalid_neighbors += 1
            if invalid_neighbors == 2:
                stop = True
        i += 1

    # plt.imshow(distances)
    # plt.show()

    nb_steps = np.max(distances)
    toc = time.time()
    print('number of steps to farthest point:', nb_steps)
    print('time:', toc-tic)
