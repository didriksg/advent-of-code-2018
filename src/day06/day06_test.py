import unittest

from src.utils import Inputstr
from src.day06 import day06 as day


class Day06TestCase(unittest.TestCase):
    def setUp(self):
        self.inputs = Inputstr("06", test=True).split("\n")

    def test_part_1(self):
        part_1_result = day.part_1(self.inputs)
        expected_output = 17
        self.assertEqual(part_1_result, expected_output)

    def test_part_2(self):
        part_2_result = day.part_2(self.inputs)
        expected_output = ""
        self.assertEqual(part_2_result, expected_output)


if __name__ == '__main__':
    unittest.main()