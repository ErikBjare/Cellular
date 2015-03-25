import unittest

from .grid import *
from .rules import *
from . import patterns


class ConwayTest(unittest.TestCase):
    def setUp(self):
        self.grid = new_grid(8, 8)

    def test_glider(self):
        init_grid(self.grid, patterns.GLIDER)
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


class CircuitTest(unittest.TestCase):
    def setUp(self):
        self.grid = new_grid(5, 13)
        init_grid(self.grid, patterns.CIRCUIT_TRACK)

    def test_basic(self):
        self.grid[1][4] = 2
        self.grid[1][3] = 3
        self.grid = apply_rule(self.grid, rule_circuit)
        self.assertEquals(self.grid[1][5], 2)
        self.assertEquals(self.grid[1][4], 3)
    
    def test_turn(self):
        self.grid[1][8] = 2
        self.grid[1][7] = 3
        for _ in range(7):
            self.grid = apply_rule(self.grid, rule_circuit)
            print_grid(self.grid, digits=True)

        self.assertEquals(self.grid[3][7], 2)
        self.assertEquals(self.grid[3][8], 3)
   
    def test_split(self):
        self.grid[1][7] = 2
        self.grid[1][8] = 3
        self.grid[2][6] = 1
        print_grid(self.grid, digits=True)
        for _ in range(3):
            self.grid = apply_rule(self.grid, rule_circuit)
            print_grid(self.grid, digits=True)
        
        # Check left track
        self.assertEquals(self.grid[1][4], 2)
        self.assertEquals(self.grid[1][5], 3)

        # Check down track
        self.assertEquals(self.grid[3][6], 2)
        self.assertEquals(self.grid[2][6], 3)

    def test_transistor(self):
        # Tests a component with transistor-like behavior
        pass

if __name__ == "__main__":
    unittest.main()
