from .grid import *

class UnexpectedCellException(Exception):
    pass


# Rule application helper functions

def compute_rule_diff(grid, rule, *args, **kwargs):
    changes = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = rule(grid, row, col, *args, **kwargs)
            if cell != grid[row][col]:
                changes[(row, col)] = cell
    return changes

def apply_diff(grid, diff):
    for k, cell in diff.items():
        grid[k[0]][k[1]] = cell
    return grid


def apply_rule(grid, rule, *args, **kwargs):
    diff = compute_rule_diff(grid, rule, *args, **kwargs)
    return apply_diff(grid, diff)


# Rules

def rule_conway(grid, i, j):
    n = sum(neighbors(grid, i, j))
    if grid[i][j]:
        # Cell is alive
        return 1 if 1 < n < 4 else 0
    else:
        # Cell is dead
        return 1 if n == 3 else 0

def rule_refractor(grid, i, j):
    # Excitable medium
    # https://en.wikipedia.org/wiki/Excitable_medium
    if grid[i][j] == 0:
        nc = neighbors_cross(grid, i, j)
        nc2 = neighbors_cross(grid, i, j, steps=2)
        if any([(nc[i] == 1) and (nc2[i] == -1) for i in range(4)]):
            return 1
        else:
            return 0
        #return 1 if sum(nn) == 0 and 1 in nn else 0
    elif grid[i][j] < 0:
        # Cell is refractory, remaining refractory period is subracted by one
        return grid[i][j] + 1
    elif grid[i][j] > 0:
        # Cell is excited, becomes refractory
        return -1

def rule_circular(grid, i, j, n):
    next_state = (grid[i][j]+1) % n
    if next_state in neighbors(grid, i, j):
        return next_state
    return grid[i][j]

def rule_circuit(grid, i, j):
    """
    Implementation of circuitlife

    States:
     0 - Dead, not part of circuit (an isolator)
     1 - Dead, part of circuit (conductor)
     2 - Alive
     3 - Refractory
    """
    if grid[i][j] == 0:
        # Cell is not part of circuit (isolator)
        return grid[i][j]
    elif grid[i][j] == 1:
        # Cell is part of circuit and not excited or refractory
        nc = neighbors_cross(grid, i, j)
        if sum(map(lambda x: 1 if x == 2 else 0, nc)) > 0:
            # Cell has one alive neighbor
            return 2
        else:
            # Cell has no alive neighbors
            return 1
    elif grid[i][j] == 2:
        # Cell is alive, make refactory
        return 3
    elif grid[i][j] == 3:
        # Cell is refractory, return to dead conductor
        return 1
    else:
        raise UnexpectedCellException("Should never happen")
