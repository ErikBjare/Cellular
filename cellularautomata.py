import unittest
from itertools import combinations
from copy import deepcopy, copy
from time import sleep
import random

def neighbors(g, r, c):
    r1, r2, r3 = ((r+offset) % len(g) for offset in (-1, 0, 1))
    c1, c2, c3 = ((c+offset) % len(g[0]) for offset in (-1, 0, 1))
    return [g[r1][c1], g[r1][c2], g[r1][c3],
            g[r2][c1],            g[r2][c3],
            g[r3][c1], g[r3][c2], g[r3][c3]]
    
def neighbors_cross(g, r, c, steps=1):
    r1, r2, r3 = ((r+offset) % len(g) for offset in (-steps, 0, steps))
    c1, c2, c3 = ((c+offset) % len(g[0]) for offset in (-steps, 0, steps))
    return [          g[r1][c2],
           g[r2][c1],           g[r2][c3],
                      g[r3][c2]]

def neighbors_neumann(g, r, c):
    inner = neighbors_cross(g, r, c)
    outer = neighbors_cross(g, r, c, steps=2)
    return [outer[0], inner[0], outer[1], inner[1], inner[2], outer[2], inner[3], outer[3]]

def rule_conway(grid, i, j):
    n = sum(neighbors(grid, i, j))
    if grid[i][j]:
        # Cell is alive
        return 1 if 1 < n < 4 else 0
    else:
        # Cell is dead
        return 1 if n == 3 else 0

def apply_rule(grid, rule, *args, **kwargs):
    changes = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = rule(grid, row, col, *args, **kwargs)
            if cell != grid[row][col]:
                changes[(row, col)] = cell
    for k, cell in changes.items():
        grid[k[0]][k[1]] = cell
    return grid

def rule_refractor(grid, i, j):
    # Excitable medium
    # https://en.wikipedia.org/wiki/Excitable_medium
    if grid[i][j] == 0:
        nn = neighbors_neumann(grid, i, j)
        nc = neighbors_cross(grid, i, j)
        directions = [nn[i:i+2] for i in range(4)]
        if any([(sum(directions[i]) == 0) and (nc[i] == 1) for i in range(4)]):
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

GLIDER = [[0, 1, 0],
          [1, 0, 0],
          [1, 1, 1]]

def init_grid(grid, init_state):
    drow = int(len(grid)/2)
    dcol = int(len(grid[0])/2)
    dirow = int(len(init_state)/2)
    dicol = int(len(init_state[0])/2)
    for row in range(len(init_state)):
        for col in range(len(init_state)):
            grid[drow+row-dirow][dcol+col-dicol] = init_state[row][col]
    return grid

def new_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def print_grid(grid, digits=False):
    print("/" + "-"*len(grid[0]) + "\\")
    for row in range(len(grid)):
        print("|", end="")
        for col in range(len(grid[0])):
            if digits:
                print(grid[row][col], end="")
            else:
                if grid[row][col] > 0:
                    print("+", end="")
                elif grid[row][col] == 0:
                    print(" ", end="")
                else:
                    print("-", end="")
        print("|")
    print("\\" + "-"*len(grid[0]) + "/")

def randomize_grid(grid, lower=0, upper=1):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = random.randint(lower, upper)

class ConwayTest(unittest.TestCase):
    def setUp(self):
        self.grid = new_grid(8, 8)

    def test_glider(self):
        init_grid(self.grid, GLIDER)
        apply_rule(self.grid, rule_conway)
       
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if (row, col) in [(4,3), (4,5), (5,3), (5,4), (6,4)]:
                    self.assertEqual(self.grid[row][col], 1)
                else:
                    self.assertEqual(self.grid[row][col], 0)

class RefractorTest(unittest.TestCase):
    def setUp(self):
        self.grid = new_grid(15, 15)

    def test_print(self):
        randomize_grid(self.grid, -1, 1)
        for _ in range(10):
            print_grid(self.grid)
            self.grid = apply_rule(self.grid, rule_refractor)


class CircularTest(unittest.TestCase):
    def setUp(self):
        self.grid = new_grid(15, 15)

    def test_print(self):
        randomize_grid(self.grid, 0, 5)
        for _ in range(10):
            print_grid(self.grid, digits=True)
            self.grid = apply_rule(self.grid, rule_circular, n=5)
        
def main():
    rows = 10
    cols = 10
    grid = new_grid(rows, cols)
    grid = init_grid(grid, GLIDER)
    for _ in range(10):
        print_grid(grid)
        grid = apply_rule(grid, rule_refractor)
        sleep(0.1)

if __name__ == "__main__":
    main()
