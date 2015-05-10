from time import sleep
import sys
import argparse

from .grid import *
from .patterns import *
from .rules import *

from . import examples


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
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--example', dest='example',
                        help='specify an example to run')
    parser.add_argument('--from-stdin', dest='from_stdin', action='store_const',
                        const=True, default=False,
                        help='load pattern from stdin')

    args = parser.parse_args()

    if args.example:
        examples.run_example(args.example)
    elif args.from_stdin:
        pattern_from_stdin()
    else:
        examples.glider_gun()


if __name__ == "__main__":
    main()
