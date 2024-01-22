import numpy as np
import time


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        notes = f.read().splitlines()

    ## read patterns as individual np arrays
    patterns = []
    pattern = []
    for i,row in enumerate(notes):
        if not row or i == len(notes)-1:
            patterns.append(np.array(pattern))
            pattern = []
        else:
            pattern.append(list(row))

    sum_reflexions = 0
    for pattern in patterns:
        ## first look for horizontal symmetry axis
        horz = 0
        for i in range(pattern.shape[0]-1):
            if all(pattern[i,:] == pattern[i+1,:]):
                k = 1
                global_symmetry = True
                while i-k >= 0 and i+k+1 < pattern.shape[0]:
                    if not all(pattern[i-k,:] == pattern[i+k+1,:]):
                        global_symmetry = False
                        break
                    k += 1
                if global_symmetry:
                    horz = i+1
                    break

        ## if none found, look to vertical symmetry axis
        vert = 0
        if horz == 0:
            for j in range(pattern.shape[1]-1):
                if all(pattern[:,j] == pattern[:,j+1]):
                    k = 1
                    global_symmetry = True
                    while j-k >= 0 and j+k+1 < pattern.shape[1]:
                        if not all(pattern[:,j-k] == pattern[:,j+k+1]):
                            global_symmetry = False
                            break
                        k += 1
                    if global_symmetry:
                        vert = j+1
                        break

        sum_reflexions += 100*horz + vert

    toc = time.time()
    print('reflexion count:', sum_reflexions)
    print('time:', toc-tic)
