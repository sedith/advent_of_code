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
    nb_const = [len(cr) for cr in col_rows]
    # for each row i, store which x_j appears in it
    row_cols = [[j for j, v in enumerate(row) if v] for row in A]
    # max_possible [0 for ]

    optimal_cost = float("inf")
    unassigned = [True] * n

    def dfs(residual: list[int], cost: int, left: int) -> None:
        nonlocal optimal_cost

        ## if leaf node, update optimal cost iff the solution is valid (residual = 0)
        if not left:
            if all(r == 0 for r in residual):
                optimal_cost = min(optimal_cost, cost)
            return

        ## in the same for-loop:
        ## cpt upper bounds for unassigned vars
        ## pick unassigned variable with smallest ub, tie-break by most constraints
        ub = [0] * n
        j = None
        best_key = None
        for k in range(n):
            if not unassigned[k]:
                continue
            ## upper bound
            if col_rows[k]:
                ub[k] = min(residual[i] for i in col_rows[k])
            ## best next variable
            key = (ub[k], -nb_const[k])
            if best_key is None or key < best_key:
                best_key = key
                j = k
                
        ## row feasibility: residual[i] must be reachable using unassigned variables
        for i in range(m):
            if residual[i] > sum(ub[k] for k in row_cols[i] if unassigned[k]):
                return

        ## explore branch
        unassigned[j] = False
        for val in range(0, ub[j] + 1):
            ## skip node if worst than current best
            if cost + val >= optimal_cost:
                break

            new_res = residual[:]  # copy prevents branches interfering with each other
            for i in col_rows[j]:
                if (r := new_res[i] - val) < 0:
                    break
                new_res[i] = r
            else:
                dfs(new_res, cost + val, left - 1)
        unassigned[j] = True

    dfs(b[:], 0, n)
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
