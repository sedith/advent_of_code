import numpy as np
import time


ACTIONS = {'U': np.array([0,1]), 'D': np.array([0,-1]), 'L': np.array([-1,0]), 'R': np.array([1,0])}
CODE_TO_ACTION = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def read_hexa(code):
    dir = CODE_TO_ACTION[code[-1]]
    length = int(code[:-1], 16)
    return dir, length


def dig_trench(plan):
    polygon = np.zeros((len(plan)+1, 2), dtype=np.int64)
    cursor = np.array([0,0])

    for i, (dir, length) in enumerate(plan):
        cursor += ACTIONS[dir] * length
        polygon[i+1,:] = cursor

    return polygon


def area_polygon(p):
    """https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon#"""
    ## Green's theorem (planimeter)
    area = 0
    for i in range(len(p)):
        j = (i+1) % len(p)
        area += p[i][0] * p[j][1] - p[i][1] * p[j][0]
    area = abs(area/2)

    return area


def segments(p):
    return zip(p, p[1:] + [p[0]])


def check_intersect(ab, cd):
    """https://stackoverflow.com/questions/7069420/check-if-two-line-segments-are-colliding-only-check-if-they-are-intersecting-n#"""
    checkside_c = np.sign( (ab[1][0] - ab[0][0]) * (cd[0][1] - ab[1][1]) - (ab[1][1] - ab[0][1]) * (cd[0][0] - ab[1][0]) )
    checkside_d = np.sign( (ab[1][0] - ab[0][0]) * (cd[1][1] - ab[1][1]) - (ab[1][1] - ab[0][1]) * (cd[1][0] - ab[1][0]) )

    checkside_a = np.sign( (cd[1][0] - cd[0][0]) * (ab[0][1] - cd[1][1]) - (cd[1][1] - cd[0][1]) * (ab[0][0] - cd[1][0]) )
    checkside_b = np.sign( (cd[1][0] - cd[0][0]) * (ab[0][1] - cd[1][1]) - (cd[1][1] - cd[0][1]) * (ab[1][0] - cd[1][0]) )

    return (checkside_c * checkside_d) < 0 and (checkside_a * checkside_b) < 0


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        plan_text = f.readlines()

    plan = []
    for step in plan_text:
        _, _, color = step.split(' ')
        code = color[2:-2]
        dir, length = read_hexa(code)
        plan.append((dir, length))

    polygon = dig_trench(plan)

    # ## check self intersections
    # segs = list(segments(polygon))
    # intersec = False
    # for s0 in segs:
    #     for s1 in segs:
    #         intersec = intersec or check_intersect(s0, s1)
    #         if intersec: break

    ## compute area
    inner_area = area_polygon(polygon)

    ## add area of trench
    trench_length = 0
    for i in range(len(polygon)):
        j = (i+1) % len(polygon)
        trench_length += abs(polygon[j][0] - polygon[i][0]) + abs(polygon[j][1] - polygon[i][1])

    ## Pick's theorem - find the number of points in a shape given its area
    ## e.g., add the half area of the trench to the mathematical area of the polygon
    inner_area = int(abs(inner_area) - 0.5 * trench_length + 1)

    volume = inner_area + trench_length  # yes, I know what you think

    toc = time.time()
    print('lava volume:', volume)
    print('time:', toc-tic)
