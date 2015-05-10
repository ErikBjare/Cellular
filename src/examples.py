from time import sleep

from .grid import *
from .rules import *
from .patterns import *


_examples = {}

def example(f):
    """A decorator that registers a function as an example"""
    _examples[f.__name__] = f
    return f

@example
def glider_gun():
    rows = 30
    cols = 60
    grid = Grid(rows, cols)
    grid.write_pattern(GLIDER_GUN)
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_conway)
        sleep(0.1)

@example
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

@example
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

@example
def highlife_replicator():
    rows = 40
    cols = 40
    grid = Grid(rows, cols)
    grid.write_pattern(HIGHLIFE_REPLICATOR)
    while True:
        grid.print(pos_cursor=True)
        grid = apply_rule(grid, rule_highlife)
        sleep(0.1)

def run_example(name):
    _examples[name]()
