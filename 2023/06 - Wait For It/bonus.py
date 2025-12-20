import numpy as np
import time
import qpsolvers


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        sheet = f.read().replace(' ', '').splitlines()

    T = int(sheet[0].split(':')[1])

    # max_dist = 0
    # optimal_press_time = 0
    # cases = range(1,T)  # segment open to both ends since those are degenerate (0 travel distance)
    # for press_T in cases:
    #     V = press_T
    #     if (D := V * (T - press_T)) > max_dist:
    #         max_dist = D
    #         optimal_press_time = press_T
    #
    # toc = time.time()
    # print('maximum distance:', max_dist)
    # print('with press time:', optimal_press_time)
    # print('time:', toc-tic)

    ## eq - x**2 + x*T = D
    ## QP
    ## min  1/2 x.T [-1] x + [1] x
    ##  st  0 < x < T
    ## so:
    ## max  1/2 x.T [1] x + [-1] x
    ##  st  0 < x < T
    tic = time.time()
    optimal_press_time_qp = qpsolvers.solve_qp(np.array([]).reshape((1,1)), np.array([-1]), lb=np.array([0]), ub=np.array([T]), solver='osqp')
    toc = time.time()

    print('qp sol:', optimal_press_time_qp)
    print('time:', toc-tic)
