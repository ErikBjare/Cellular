from time import sleep

from .grid import *
from .rules import *
from .patterns import *
       


def main():
    rows = 30
    cols = 60
    grid = new_grid(rows, cols)
    grid = init_grid(grid, GLIDER_GUN)
    for _ in range(50):
        print_grid(grid)
        grid = apply_rule(grid, rule_conway)
        sleep(0.2)

if __name__ == "__main__":
    main()
