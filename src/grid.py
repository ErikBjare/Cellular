import random

import colorama
from colorama import Fore
colorama.init()

# Neighbors helper functions

def neighbors(g, r, c):
    """
    Returns the Moore neighborhood
    .....
    .xxx.
    .xcx.
    .xxx.
    .....

    https://en.wikipedia.org/wiki/File:CA-Moore.png
    """
    r1, r2, r3 = ((r+offset) % len(g) for offset in (-1, 0, 1))
    c1, c2, c3 = ((c+offset) % len(g[0]) for offset in (-1, 0, 1))
    return [g[r1][c1], g[r1][c2], g[r1][c3],
            g[r2][c1],            g[r2][c3],
            g[r3][c1], g[r3][c2], g[r3][c3]]
    
def neighbors_cross(g, r, c, steps=1):
    """
    Returns the immediate von Neumann neighborhood.

    .....
    ..x..
    .xcx.
    ..x..
    .....

    You can use steps=2 to instead get the 4 cells included in the extended neighborhood.

    ..x..
    .....
    x.c.x
    .....
    ..x..

    https://en.wikipedia.org/wiki/File:CA-von-Neumann.png
    """
    r1, r2, r3 = ((r+offset) % len(g) for offset in (-steps, 0, steps))
    c1, c2, c3 = ((c+offset) % len(g[0]) for offset in (-steps, 0, steps))
    return [          g[r1][c2],
           g[r2][c1],           g[r2][c3],
                      g[r3][c2]]

def neighbors_neumann_extended(g, r, c):
    """Returns the entire extended von Neumann neighborhood"""
    inner = neighbors_cross(g, r, c)
    outer = neighbors_cross(g, r, c, steps=2)
    return [outer[0], inner[0], outer[1], inner[1], inner[2], outer[2], inner[3], outer[3]]


# Grid functions

def _position_cursor(row, col):
    print("\033[" + str(row) + ";" + str(col) + "H", end="")

def _clear_term():
    print("\033[2J", end="")

class Grid():
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        return self._grid[index]

    def __len__(self):
        return self._rows

    def write_pattern(self, pattern):
        if len(pattern) > self._rows or len(pattern[0]) > self._cols:
            raise Exception("Grid size too small for given initializer state")
        drow = int(self._rows/2)
        dcol = int(self._cols/2)
        dirow = int(len(pattern)/2)
        dicol = int(len(pattern[0])/2)
        for row in range(len(pattern)):
            for col in range(len(pattern[0])):
                self[drow+row-dirow][dcol+col-dicol] = pattern[row][col]

    def randomize(self, lower=0, upper=1):
        for row in range(self._rows):
            for col in range(self._cols):
                self[row][col] = random.randint(lower, upper)

    def print(self, digits=False, color=True, pos_cursor=False):
        # TODO: Detect if terminal supports color
        if pos_cursor:
            _clear_term()
            _position_cursor(1, 1)
        print("/" + "-"*self._cols + "\\")
        for row in range(self._rows):
            print(Fore.RESET + "|", end="")
            for col in range(self._cols):
                if digits:
                    print(self[row][col], end="")
                else:
                    if self[row][col] > 0:
                        print(Fore.GREEN + str(self[row][col]), end="")
                    elif self[row][col] == 0:
                        print(Fore.RESET + " ", end="")
                    else:
                        print(Fore.YELLOW + "-", end="")
            print(Fore.RESET + "|")
        print("\\" + "-"*self._cols + "/")
