from time import sleep
import sys

from .grid import *
from .rules import *
from .patterns import *
       

def glider_gun():
    rows = 30
    cols = 60
    grid = Grid(rows, cols)
    grid.write_pattern(GLIDER_GUN)
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_conway)
        sleep(0.1)

def circuit():
    rows = 5
    cols = 15
    grid = Grid(rows, cols)
    grid.write_pattern(CIRCUIT_TRACK)
    grid[1][3] = 2
    grid[1][4] = 3
    grid[2][7] = 3
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_circuit)
        sleep(0.1)

def highlife_replicator():
    rows = 40
    cols = 40
    grid = Grid(rows, cols)
    grid.write_pattern(HIGHLIFE_REPLICATOR)
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_highlife)
        sleep(0.1)

def main():
    if len(sys.argv) == 1:
        glider_gun()
    else:
        if sys.argv[1] == "glider":
            glider_gun()
        elif sys.argv[1] == "circuit":
            circuit()
        elif sys.argv[1] == "highlife":
            highlife_replicator()


if __name__ == "__main__":
    main()
