import unittest

from src.day05 import day05 as day
from src.utils import Inputstr


class Day05TestCase(unittest.TestCase):
    def setUp(self):
        self.cs = day.create_containing_set()
        self.input_str = Inputstr("05", test=True)

    def test_part_1_small_remove_pair(self):
        testing_data = "aA"
        result = day.part_1(testing_data, self.cs)
        self.assertEqual(result, "")
        self.assertEqual(len(result), 0)

    def test_part_1_small_remove_after_removal(self):
        testing_data = "abBA"
        result = day.part_1(testing_data, self.cs)
        self.assertEqual(result, "")
        self.assertEqual(len(result), 0)

    def test_part_1_small_no_remove(self):
        testing_data = "abAB"
        result = day.part_1(testing_data, self.cs)
        self.assertEqual(result, "abAB")
        self.assertEqual(len(result), 4)

    def test_part_1_small_no_remove_equal_case(self):
        testing_data = "aabAAB"
        result = day.part_1(testing_data, self.cs)
        self.assertEqual(result, "aabAAB")
        self.assertEqual(len(result), 6)

    def test_part_1_large(self):
        non_reactive_string = day.part_1(self.input_str, self.cs)
        self.assertEqual(non_reactive_string, "dabCBAcaDA")
        self.assertEqual(len(non_reactive_string), 10)

    def test_part_2_large(self):
        shortest_non_reactive = day.part_2(self.input_str, self.cs)
        self.assertEqual(shortest_non_reactive, "daDA")
        self.assertEqual(len(shortest_non_reactive), 4)

    def test_containing_set(self):
        cs = day.create_containing_set()
        self.assertEqual(len(cs), 26 * 2)


if __name__ == '__main__':
    unittest.main()
