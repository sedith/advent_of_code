def naive_solution(l1, l2):
    score = 0
    for n1 in l1:
        score += n1 * sum([n2 == n1 for n2 in l2])
    return score


def better_solution(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)

    mem = {}
    score = 0
    cursor = 0

    for n1 in l1:
        if n1 not in mem.keys():
            mem[n1] = 0
            while cursor < len(l2) and l2[cursor] < n1:
                cursor += 1
            while cursor < len(l2) and l2[cursor] == n1:
                cursor += 1
                mem[n1] += 1
        score += n1 * mem[n1]
    return score


def main(data):
    lists = map(lambda x: [int(n) for n in x.split()], data)
    lists = list(map(list, zip(*lists)))  # transpose
    l1 = lists[0]
    l2 = lists[1]

    # return naive_solution(l1, l2)  # 23ms
    return better_solution(l1, l2)  # 1ms


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
