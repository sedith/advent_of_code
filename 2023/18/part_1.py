import numpy as np
import time
import matplotlib.pyplot as plt


MAP_VALS = {'none': 0, 'trench': 1, 'in': 2, 'out': 3}
ACTIONS = {'U': np.array([0,-1]), 'D': np.array([0,1]), 'L': np.array([-1,0]), 'R': np.array([1,0])}
CODE_TO_ACTION = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

def increase_map(map, map_center, cursor):
    ## add col to left
    if map_center[0] + cursor[0] < 0:
        col = np.zeros((map.shape[0], 1), dtype=np.int8)
        map = np.hstack([col, map])
        map_center[0] += 1
    ## add col to right
    if map_center[0] + cursor[0] >= map.shape[1]:
        col = np.zeros((map.shape[0], 1), dtype=np.int8)
        map = np.hstack([map, col])
    ## add row to top
    if map_center[1] + cursor[1] < 0:
        row = np.zeros((1, map.shape[1]), dtype=np.int8)
        map = np.vstack([row, map])
        map_center[1] += 1
    ## add row to bottom
    if map_center[1] + cursor[1] >= map.shape[0]:
        row = np.zeros((1, map.shape[1]), dtype=np.int8)
        map = np.vstack([map, row])

    return map, map_center


def dig_trench(plan):
    map = np.zeros((1,1), dtype=np.int8)
    map_center = np.array([0,0])
    cursor = np.array([0,0])

    for dir, length in plan:
        for i in range(int(length)):
            ## move cursor
            cursor += ACTIONS[dir]

            ## increase map size in necessary
            map, map_center = increase_map(map, map_center, cursor)

            ## update map
            idx = tuple(map_center+cursor)
            map[idx[1], idx[0]] = MAP_VALS['trench']
    return map, (map_center[1], map_center[0])


def dig_interior(map):
    for i in range(map.shape[0]):
        switch = False
        memory = None  # stores the "u" or "n" value for switches
        for j in range(map.shape[1]):
            if map[i,j] != MAP_VALS['trench']:
                map[i,j] = MAP_VALS['out'] if not switch else MAP_VALS['in']
            else:
                ## switch when crossing the trench
                if j == 0 or map[i,j-1] != MAP_VALS['trench']:
                    if i >= 0 and map[i-1,j] == MAP_VALS['trench']:
                        memory = 'u'
                    else:
                        memory = 'n'
                    switch = not switch
                ## unswitch in "u" or "n" cases
                if j != map.shape[1]-1 and map[i,j-1] == MAP_VALS['trench'] and map[i,j+1] != MAP_VALS['trench']:
                    if memory is None:
                        print('you should not be here!')
                    if memory == 'u' and map[i-1,j] == MAP_VALS['trench']:  # i>0 already tested when setting memory
                        switch = not switch
                    if memory == 'n' and i < map.shape[0] and map[i+1,j] == MAP_VALS['trench']:
                        switch = not switch
                    memory = None
    return map


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        plan_text = f.readlines()

    plan = []
    for step in plan_text:
        dir, length, _ = step.split(' ')
        plan.append((dir, length))

    map, _ = dig_trench(plan)
    map = dig_interior(map)

    vol_trench = np.count_nonzero(map == MAP_VALS['trench'])
    vol_in = np.count_nonzero(map == MAP_VALS['in'])

    toc = time.time()
    print('lava volume:', vol_trench + vol_in)
    print('time:', toc-tic)

    plt.imshow(map)
    plt.show()
