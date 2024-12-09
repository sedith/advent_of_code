def _rec_check(possibilies, numbers):
    if not numbers:
        return possibilies
    if not possibilies:
        possibilies.append(numbers[0])
    else:
        for i in range(len(possibilies)):
            sum = possibilies[i] + numbers[0]
            mul = possibilies[i] * numbers[0]
            possibilies[i] = sum
            possibilies.append(mul)
    return _rec_check(possibilies, numbers[1:])


def main(data):
    sum_calib = 0
    for equation in data:
        result, numbers = equation.split(':')
        result = int(result)
        numbers = list(map(int, numbers.split()))

        possibilies = _rec_check([], numbers)
        sum_calib += result * (result in possibilies)

    return sum_calib


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
