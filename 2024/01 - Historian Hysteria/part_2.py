import time


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


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
    lists = map(lambda x: [int(n) for n in x.split()], input)
    lists = list(map(list, zip(*lists)))  # transpose
    l1 = lists[0]
    l2 = lists[1]

    # score = naive_solution(l1, l2)  # 23ms
    score = better_solution(l1, l2)  # 1ms

    toc = time.time()
    print('similarity score:', score)
    print('time:', toc-tic)
