import re


mult_s = 'mul\(\d{1,3},\d{1,3}\)'
do_s = 'do()'
dont_s = 'don\'t()'


def re_sol(input):
    do_s_re = do_s.replace('(', '\(').replace(')', '\)')
    dont_s_re = dont_s.replace('(', '\(').replace(')', '\)')

    sum_mult = 0
    do = True
    for line in input:
        nums = re.compile(f'{mult_s}|{do_s_re}|{dont_s_re}')
        while (match := nums.search(line)) is not None:
            match_str = match.group(0)
            if match_str == do_s:
                do = True
            elif match_str == dont_s:
                do = False
            elif do:
                n1, n2 = match_str[4:-1].split(',')
                sum_mult += int(n1) * int(n2)
            line = line[match.start() + len(match_str) :]
    return sum_mult


def manual_sol(input):
    sum_mult = 0
    do = True
    last = ''
    n1 = ''
    n2 = ''
    for line in input:
        for c in line:
            if c == 'd':
                last = 'd'
            elif do and c == 'm':
                last = 'm'
            elif last == 'd' and c == 'o':
                last = 'do'
            elif last == 'do' and c == '(':
                last = 'do('
            elif last == 'do(' and c == ')':
                last = ''
                do = True
            elif last == 'do' and c == 'n':
                last = 'don'
            elif last == 'don' and c == '\'':
                last = 'don\''
            elif last == 'don\'' and c == 't':
                last = 'don\'t'
            elif last == 'don\'t' and c == '(':
                last = 'don\'t('
            elif last == 'don\'t(' and c == ')':
                last = ''
                do = False
            elif last == 'm' and c == 'u':
                last = 'mu'
            elif last == 'mu' and c == 'l':
                last = 'mul'
            elif last == 'mul' and c == '(':
                last = 'mul('
            elif last == 'mul(' and c.isdigit() and len(n1) < 3:
                n1 += c
            elif last == 'mul(' and c == ',':
                last = 'mul(,'
            elif last == 'mul(,' and c.isdigit() and len(n2) < 3:
                n2 += c
            elif last == 'mul(,' and c == ')' and len(n1) and len(n2):
                sum_mult += int(n1) * int(n2)
                n1 = ''
                n2 = ''
                last = ''
            else:
                n1 = ''
                n2 = ''
                last = ''
    return sum_mult


def main(data):
    return re_sol(data)
    # return manual_sol(data)


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
