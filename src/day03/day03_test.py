import unittest
import numpy as np

from src.utils import Inputstr
from src.day03 import day03


class Day03TestCase(unittest.TestCase):
    def setUp_trial(self):
        self.raw_lines = Inputstr("03", test=True).split("\n")
        self.line_info = [line.split(" ")[2:] for line in self.raw_lines]

        self.area_size = 1000
        self.total_map = np.zeros((self.area_size, self.area_size))
        self.total_size = [0] * (len(self.line_info) + 1)

    def setUp_actual(self):
        self.raw_lines = Inputstr("03", test=False).split("\n")
        self.line_info = [line.split(" ")[2:] for line in self.raw_lines]

        self.area_size = 1000
        self.total_map = np.zeros((self.area_size, self.area_size))
        self.total_size = [0] * (len(self.line_info) + 1)

    def test_day03_part1_test(self):
        self.setUp_trial()
        unique, counts = day03.part_1(self.total_map, self.line_info, self.total_size)
        index, = np.where(unique == -1)
        self.assertEqual(counts[index][0], 4)

    def test_part2_test(self):
        self.setUp_trial()
        unique, counts = day03.part_1(self.total_map, self.line_info, self.total_size)
        unique_int = [int(i) for i in unique]
        non_overlap_id = day03.part_2(self.total_size, unique_int[2:], counts[2:])

        self.assertEqual(non_overlap_id, 3)

    def test_part1_actual(self):
        self.setUp_actual()
        unique, counts = day03.part_1(self.total_map, self.line_info, self.total_size)
        index, = np.where(unique == -1)
        self.assertEqual(counts[index][0], 100261)

    def test_part2_actual(self):
        self.setUp_actual()
        unique, counts = day03.part_1(self.total_map, self.line_info, self.total_size)
        unique_int = [int(i) for i in unique]
        non_overlap_id = day03.part_2(self.total_size, unique_int[2:], counts[2:])

        self.assertEqual(non_overlap_id, 251)

if __name__== '__main__':
    unittest.main()