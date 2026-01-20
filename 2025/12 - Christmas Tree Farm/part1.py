from math import prod


def main(data):
    present_size = []
    nb_valid_regions = 0

    for line in data:
        ## first get the 'size' of each present (nb of #)
        if line.strip().endswith(":"):
            present_size.append(0)
        elif '#' in line:
            present_size[-1] += line.count('#')

        ## count regions whose area is smaller than the total present area
        elif 'x' in line:
            region_area, quantities = line.split(':')
            region_area = prod(map(int, region_area.split('x')))

            present_area = sum(nb * present_size[id] for id, nb in enumerate(map(int, quantities.split())))

            nb_valid_regions += (present_area <= region_area)
    return nb_valid_regions


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
