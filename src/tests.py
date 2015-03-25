import unittest

from .grid import *
from .rules import *
from .patterns import *


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

    def test_basic(self):
        randomize_grid(self.grid, -1, 1)
        for _ in range(10):
            #print_grid(self.grid)
            self.grid = apply_rule(self.grid, rule_refractor)

    def test_wave(self):
        """Tests a simple (width=1) wave"""
        self.grid[10][10] = 1
        self.grid[10][9] = -1
        apply_rule(self.grid, rule_refractor)
        self.assertEqual(self.grid[10][11], 1)
        self.assertEqual(self.grid[10][10], -1)



class CircularTest(unittest.TestCase):
    def setUp(self):
        self.grid = new_grid(15, 15)

    def test_basic(self):
        randomize_grid(self.grid, 0, 5)
        for _ in range(10):
            #print_grid(self.grid, digits=True)
            self.grid = apply_rule(self.grid, rule_circular, n=5)

if __name__ == "__main__":
    unittest.main()
