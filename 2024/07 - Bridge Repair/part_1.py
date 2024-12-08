import time


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


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    sum_calib = 0
    for equation in data:
        result, numbers = equation.split(':')
        result = int(result)
        numbers = list(map(int,numbers.split()))

        possibilies = _rec_check([], numbers)
        sum_calib += result * (result in possibilies)

    toc = time.time()
    print('sum of calibration results:', sum_calib)
    print('time:', toc-tic)
