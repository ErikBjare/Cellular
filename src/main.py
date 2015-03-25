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

def wireworld():
    rows = 5
    cols = 15
    grid = Grid(rows, cols)
    grid.write_pattern(WIREWORLD_TRACK)
    grid[1][4] = 2
    grid[1][5] = 3
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_wireworld)
        sleep(0.1)

def wireworld_diodes():
    rows = 9
    cols = 12
    grid = Grid(rows, cols)

    # Write diode with input in conducting direction
    grid.write_pattern(WIREWORLD_DIODE, offset_row = -2)
    grid[2][3] = 3
    grid[2][4] = 2

    # Write diode with input from previous diode in isolating direction
    grid.write_pattern(WIREWORLD_DIODE, offset_row = 2)
    grid[6][11] = 0
    for i in range(3, 6):
        grid[i][10] = 1

    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_wireworld)
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

def pattern_from_stdin():
    # TODO: Enable choice of rule
    pattern = sys.stdin.read()
    pattern = string_to_pattern(pattern)
    grid = Grid.from_pattern(pattern)
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_conway)
        sleep(0.1)
    

def main():
    if len(sys.argv) == 1:
        glider_gun()
    else:
        if sys.argv[1] == "glider_gun":
            glider_gun()
        elif sys.argv[1] == "wireworld":
            wireworld()
        elif sys.argv[1] == "wireworld_diode":
            wireworld_diodes()
        elif sys.argv[1] == "highlife":
            highlife_replicator()
        elif sys.argv[1] == "--":
            pattern_from_stdin()


if __name__ == "__main__":
    main()
