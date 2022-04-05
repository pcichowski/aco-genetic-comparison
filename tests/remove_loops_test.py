import unittest
import sys

sys.path.append('../')

from Ant import remove_loops


class TestRemoveLoops(unittest.TestCase):
    def test_remove_loops_max(self):
        """
            Test that it can remove a large number of loops
        """
        data = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 2, 3, 4, 5,
                6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 11, 12, 13, 14, 15, 16]
        result = remove_loops(data)

        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_remove_loops_min(self):
        """
            Test that it can remove a loop from a small list
        """
        data = [1, 2, 1, 2]
        result = remove_loops(data)

        self.assertEqual(result, [1, 2])

    def test_remove_loops_general(self):
        """
            Test that it can remove a common list with loops
        """
        data = [1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10]
        result = remove_loops(data)

        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


unittest.main()
