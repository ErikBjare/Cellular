import random


# Neighbors helper functions

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


# Grid functions

def new_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def init_grid(grid, init_state):
    drow = int(len(grid)/2)
    dcol = int(len(grid[0])/2)
    dirow = int(len(init_state)/2)
    dicol = int(len(init_state[0])/2)
    for row in range(len(init_state)):
        for col in range(len(init_state[0])):
            grid[drow+row-dirow][dcol+col-dicol] = init_state[row][col]
    return grid

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
