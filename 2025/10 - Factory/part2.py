from functools import lru_cache
from math import inf


def bnb_min_sum(A: list[list[int]], b: list[int]) -> int:
    """
    branch-and-bound algorithm
    solves the problem:
        min sum(x)
        subject to A x = b
        x in N
    with
    A: list of lists (m x n) with 0/1 entries
    b: list length m, nonnegative ints
    returns optimal cost (inf in infeasible)
    """
    m, n = len(A), len(A[0])

    ## for each x_j, store in which rows it appears in
    col_rows = [[i for i, row in enumerate(A) if row[j]] for j in range(n)]
    nb_const = [len(cr) for cr in col_rows]
    # for each row i, store which x_j appears in it
    row_cols = [[j for j, v in enumerate(row) if v] for row in A]
    # max_possible [0 for ]

    @lru_cache(maxsize=None)
    def branch_dfs(residual: tuple[int, ...], mask: int) -> int:
        ## if leaf node, update optimal cost iff the solution is valid (residual = 0)
        if mask == 0:
            return 0 if all(r == 0 for r in residual) else inf

        ## in the same for-loop:
        ## cpt upper bounds for unassigned vars
        ## pick unassigned variable with smallest ub, tie-break by most constraints
        ub = {}
        best_j = None
        best_key = (inf, inf)
        for j in range(n):
            if not (mask & (1 << j)):
                continue
            ## upper bound
            ub[j] = min(residual[i] for i in col_rows[j]) if col_rows[j] else 0
            ## best next variable
            key = (ub[j], -nb_const[j])
            if key < best_key:
                best_key = key
                best_j = j
                
        ## row feasibility: residual[i] must be reachable using unassigned variables
        for i in range(m):
            max_possible = 0
            for k in row_cols[i]:
                if mask & (1 << k):
                    max_possible += ub.get(k, 0)
            if residual[i] > max_possible:
                return inf

        ## explore branch
        best = inf
        new_mask = mask & ~(1 << best_j)
        # for val in reversed(range(0, ub[j] + 1)):
        for val in range(ub[best_j] + 1):
            ## skip node if worst than current best
            if val >= best:
                break
            new_res = list(residual)  # copy prevents branches interfering with each other
            for i in col_rows[best_j]:
                if (r := new_res[i] - val) < 0:
                    break
                new_res[i] = r
            else:
                sub = branch_dfs(tuple(new_res), new_mask)
                best = min(best, val + sub)
                continue
            break
        return best

    return branch_dfs(b, (1 << n) - 1)


def parse_machine(line):
    _, *b_str, j_str = line.split()
    buttons = [tuple(map(int, t[1:-1].split(','))) for t in b_str]
    b = tuple(map(int, j_str[1:-1].split(',')))
    A = list(zip(*[[1 if i in btn else 0 for i in range(len(b))] for btn in buttons]))
    return A, b


def main(data):
    return sum([bnb_min_sum(*parse_machine(line)) for line in data])


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
