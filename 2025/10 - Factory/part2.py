def bnb_min_sum(A: list[list[int]], b: list[int]) -> int:
    """
    branch-and-bound algorithm
    solves the problem:
        min sum(x)
        subject to A x = b
        x in N
    with
    A: List of Lists (m x n) with 0/1 entries (works for nonnegative too)
    b: List length m, nonnegative ints
    returns optimal cost (inf in infeasible)
    """
    m, n = len(A), len(A[0])

    ## for each x_j, store in which rows it appears in
    col_rows = [[i for i, row in enumerate(A) if row[j]] for j in range(n)]
    # for each row i, store which x_j appears in it
    row_cols = [[j for j, v in enumerate(row) if v] for row in A]

    optimal_cost = float("inf")
    unassigned = [True] * n
    left = n

    def dfs(j: int, residual: list[int], cost: int) -> None:
        nonlocal optimal_cost

        ## if leaf node, update optimal cost iff the solution is valid (residual = 0)
        if j == n:
            if all(r == 0 for r in residual):
                optimal_cost = min(optimal_cost, cost)
            return

        ## upper bound for x[j] as min residual over rows where it appears
        ub_j = min(residual[i] for i in col_rows[j]) if col_rows[j] else 0

        ## row-feasibility interval pruning: upper bound ub_k for each unassigned variable k >= j
        ub_k = [0] * n
        for k in range(j, n):
            if col_rows[k]:
                ub_k[k] = min(residual[i] for i in col_rows[k])

        ## for each row i, residual must be <= sum of ub_k over unassigned vars in that row
        for i in range(m):
            max_possible = 0
            for k in row_cols[i]:
                if k >= j:
                    max_possible += ub_k[k]
            if residual[i] > max_possible:
                return

        ## explore branch
        for val in range(0, ub_j + 1):
            ## skip node if worst than current best
            if cost + val >= optimal_cost:
                continue

            new_res = residual[:]  # copy prevents branches interfering with each other
            for i in col_rows[j]:
                if (r := new_res[i] - val) < 0:
                    break
                new_res[i] = r
            else:
                dfs(j + 1, new_res, cost + val)

    dfs(0, b[:], 0)
    return optimal_cost


def main(data):
    sum = 0
    for i, line in enumerate(data):
        ssplit = line.split()
        buttons = [tuple(map(int, t[1:-1].split(','))) for t in ssplit[1:-1]]
        b = list(map(int, ssplit[-1][1:-1].split(',')))
        A = list(zip(*[[1 if i in btn else 0 for i in range(len(b))] for btn in buttons]))
        print(i)
        print(A)
        print(b)
        print()
        sum += bnb_min_sum(A, b)
    return sum


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
