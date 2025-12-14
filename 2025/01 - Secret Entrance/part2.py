def main(data):
    dial = 50
    nb_0 = 0
    for line in data:
        direction, distance = (1 if line[0] == 'R' else -1, int(line[1:]))
        next_dial = (dial + direction * distance)
        if next_dial % 100 == 0 and direction == -1:
            nb_0 += 1
        if dial % 100 == 0 and direction == -1:
            nb_0 -= 1
        nb_0 += abs(dial // 100 - next_dial // 100)
        dial = next_dial
    return nb_0


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
