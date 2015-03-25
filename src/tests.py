import unittest
from abc import abstractmethod

from .grid import *
from .rules import *
from . import patterns


class AutomataTest(unittest.TestCase):
    def setUp(self):
        self._first = True

    @abstractmethod
    def rule(self):
        raise NotImplementedError

    def next(self):
        if self._first:
            self.grid.print(digits=True)
            self._first = False
        self.grid = self.rule()
        self.grid.print(digits=True)


class ConwayTest(AutomataTest):
    def setUp(self):
        AutomataTest.setUp(self)
        self.grid = Grid(8, 8)

    def rule(self):
        return apply_rule(self.grid, rule_conway)

    def test_glider(self):
        self.grid.write_pattern(patterns.GLIDER)
        self.next()
       
        for row in range(len(self.grid)):
            for col in range(len(self.grid)):
                if (row, col) in [(4,3), (4,5), (5,3), (5,4), (6,4)]:
                    self.assertEqual(self.grid[row][col], 1)
                else:
                    self.assertEqual(self.grid[row][col], 0)


class RefractorTest(AutomataTest):
    def setUp(self):
        AutomataTest.setUp(self)
        self.grid = Grid(15, 15)

    def rule(self):
        return apply_rule(self.grid, rule_refractor)

    def test_basic(self):
        self.grid.randomize(-1, 1)
        for _ in range(10):
            self.next()

    def test_wave(self):
        """Tests a simple (width=1) wave"""
        self.grid[10][10] = 1
        self.grid[10][9] = -1
        self.next()
        self.assertEqual(self.grid[10][11], 1)
        self.assertEqual(self.grid[10][10], -1)


class CyclicTest(AutomataTest):
    def setUp(self):
        AutomataTest.setUp(self)
        self.grid = Grid(15, 15)
    
    def rule(self):
        return apply_rule(self.grid, rule_cyclic, n=5)

    def test_basic(self):
        self.grid.randomize(0, 5)
        for _ in range(10):
            self.next()


class WireworldTest(AutomataTest):
    def setUp(self):
        AutomataTest.setUp(self)
        self.grid = Grid(5, 13)
        self.grid.write_pattern(patterns.WIREWORLD_TRACK)

    def rule(self):
        return apply_rule(self.grid, rule_wireworld)

    def test_basic(self):
        self.grid[1][4] = 2
        self.grid[1][3] = 3
        self.next()
        self.assertEquals(self.grid[1][5], 2)
        self.assertEquals(self.grid[1][4], 3)
    
    def test_turn(self):
        self.grid[1][8] = 2
        self.grid[1][7] = 3
        for _ in range(5):
            self.next()

        self.assertEquals(self.grid[3][7], 2)
        self.assertEquals(self.grid[3][8], 3)
   
    def test_split(self):
        self.grid[1][7] = 2
        self.grid[1][8] = 3
        self.grid[2][6] = 1
        for _ in range(2):
            self.next()
        
        # Check left track
        self.assertEquals(self.grid[1][5], 2)
        self.assertEquals(self.grid[1][6], 3)

        # Check down track
        self.assertEquals(self.grid[3][6], 2)
        self.assertEquals(self.grid[2][6], 3)

    def test_transistor(self):
        # Tests a component with transistor-like behavior
        pass


if __name__ == "__main__":
    unittest.main()
