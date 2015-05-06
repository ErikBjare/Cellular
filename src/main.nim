# Cellular
#
# A cellular automata engine
#
# I watched the following a lot while writing this:
#   https://github.com/henrybw/nim-life
#
# I was also heavily inspired by my previous Python implementation

import parseopt2

from sequtils import filter, newSeqWith

type
    Cell* = object
        state: int
        age: int
        liveNeighbors: int  # Cache of live neighbors used during evolution

    Universe* = object
        cells: seq[Cell]
        width, height: int
        age: int

    # TODO: Remove
    Grid[W, H: static[int]] =
        array[1..W, array[1..H, int]]

proc print[W,H](this: Grid[W,H]): void =
    echo "..."

proc neighbors[W, H](grid: Grid[W, H], i, j: int): int =
    result =
        grid[(i-1) %% high(grid)][j-1 %% high(grid[0])] +
        grid[(i-1) %% high(grid)][j] +
        grid[(i-1) %% high(grid)][j+1 %% high(grid[0])] +
        grid[i][j-1 %% high(grid[0])] +
        grid[i][j+1 %% high(grid[0])] +
        grid[(i+1) %% high(grid)][j-1 %% high(grid[0])] +
        grid[(i+1) %% high(grid)][j] +
        grid[(i+1) %% high(grid)][j+1 %% high(grid[0])]

proc conway[W, H](grid: Grid[W, H]): Grid[W, H] =
    for i in 1..high(grid):
        for j in 1..high(grid[0]):
            # TODO: Rewrite using matrix filters
            var aliveNeighbors = neighbors(grid, i, j)
            if grid[i][j] == 1:
                result[i][j] = if 1 < aliveNeighbors < 4: 1
                               else: 0
            else:
                result[i][j] = if aliveNeighbors == 3: 1
                               else: 0

proc main(): void =
    var grid = Grid[10,10]
    conway(grid)
    echo "test"


main()
