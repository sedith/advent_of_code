def main(data):
    races = list(map(lambda t: (int(t[0]), int(t[1])), zip(data[0].split()[1:], data[1].split()[1:])))  # (so legible)

    solution = 1
    for T, D in races:
        ways_to_beat = 0
        cases = range(1, T)  # segment open to both ends since those are degenerate (0 travel distance)
        for press_T in cases:
            V = press_T
            if V * (T - press_T) > D:
                ways_to_beat += 1
            elif ways_to_beat > 0:
                break
        solution *= ways_to_beat

    return solution


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
