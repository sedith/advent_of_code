from math import inf, floor, ceil


EPS = 1e-9

def simplex(Ab, c):
    """
    simplex solver for LP:
        min c^T x
        st. A x <= b
            x >= 0
    Ab: list of constraints [a1..an b], ai in {-1, 0, 1}
    c: cost vector
    returns (opt, x) or (-inf, None)
    """
    ## tableau pivoting
    def pivot(r, c):
        k = 1 / D[r][c]
        for i in range(m + 2):
            if i == r:
                continue
            for j in range(n + 2):
                if j != c:
                    D[i][j] -= D[r][j] * D[i][c] * k
        for j in range(n + 2):
            D[r][j] *= k
        for i in range(m + 2):
            D[i][c] *= -k
        D[r][c] = k
        B[r], N[c] = N[c], B[r]

    ## simplex iteration until optimal or unbounded
    def find(p):
        while True:
            if D[m+p][c := min((i for i in range(n + 1) if p or N[i] != -1), key=lambda x: (D[m+p][x], N[x]))] > -EPS: return 1
            if (r := min((i for i in range(m) if D[i][c] > EPS), key=lambda x: (D[x][-1]/D[x][c], B[x]), default=-1)) == -1: return 0
            pivot(r, c)

    m = len(Ab); n = len(Ab[0]) - 1

    B = [*range(n, n + m)]  # idx basic (slack) variables
    N = [*range(n), -1]  # idx nonbasic variables, artificial marker -1
    D = [*([*Ab[i][:-1], -1, Ab[i][-1]] for i in range(m)), c+[0]*2, [0]*(n+2)]  # tableau (rhs last col) rows: constraints, objective, phase I

    ## phase I
    D[-1][n] = 1
    r = min(range(m), key=lambda x: D[x][-1])  # most infeasible row
    if D[r][-1] < -EPS:
        pivot(r, n)
        if not find(1) or D[-1][-1] < -EPS:
            return -inf, None

    ## if artificial variable is basic, pivot it out
    for i in range(m):
        if B[i] == -1:
            pivot(i, min(range(n), key=lambda x: (D[i][x], N[x])))

    ## phase II
    if find(0):
        x = [0]*n
        for i in range(m):
            if 0 <= B[i] < n:
                x[B[i]] = D[i][-1]
        return sum(ci * xi for ci, xi in zip(c, x)), x
    else:
        return -inf, None


def bnb(A: list[list[int]], b: list[int]) -> int:
    """
    branch-and-bound algorithm using simplex for bounds
    solves the ILP:
        min c^T x
        st. A x = b
            x in N
    with
    A: list of lists (m x n), 0/1
    b: target vector (m), nonnegative ints
    c: cost vector (n), floats  -- not provided currently since trivial [1...1]
    returns optimal cost (inf in infeasible)
    """
    m, n = len(A), len(A[0])
    c = [1] * n  # objective: sum of x_i

    optimal_cost = inf
    def branch(node_constraints: list[list[int|float]]) -> None:
        nonlocal optimal_cost

        cost, x = simplex(node_constraints, c)

        ## prune
        if cost + EPS >= optimal_cost or cost == -inf:
            return

       ## find a fractional variable
        for i, xi in enumerate(x):
            if abs(xi - round(xi)) > EPS:
                k = i
                break
        else:
            ## if all integer: update optimal_cost incubent
            optimal_cost = min(cost, optimal_cost)
            return

        ## branch x_k <= floor(x_k)
        row_le = [0] * n + [floor(x[k])]
        row_le[k] = 1.0
        branch(node_constraints + [row_le])

        ## branch x_k >= ceil(x_k)
        row_ge = [0] * n + [-ceil(x[k])]
        row_ge[k] = -1
        branch(node_constraints + [row_ge])

    ## ineq constraints Ab (for simplex)
    constraints = []
    for i in range(m):
        constraints.append(A[i] + [b[i]])
        constraints.append([-a for a in A[i]] + [-b[i]])

    branch(constraints)
    return round(optimal_cost)


def parse_machine(line):
    _, *b_str, j_str = line.split()
    buttons = [list(map(int, t[1:-1].split(','))) for t in b_str]
    b = list(map(int, j_str[1:-1].split(',')))
    A = list(map(list, zip(*[[1 if i in btn else 0 for i in range(len(b))] for btn in buttons])))
    return A, b


def main(data):
    return sum([bnb(*parse_machine(line)) for line in data])


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


#####

from functools import lru_cache
def bnb_arithm(A: list[list[int]], b: list[int]) -> int:
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
