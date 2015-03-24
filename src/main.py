from time import sleep

from .grid import *
from .rules import *
from .patterns import *
        
def main():
    rows = 10
    cols = 15
    grid = new_grid(rows, cols)
    grid = init_grid(grid, GLIDER)
    for _ in range(100):
        print_grid(grid)
        grid = apply_rule(grid, rule_conway)
        sleep(0.1)

if __name__ == "__main__":
    main()
