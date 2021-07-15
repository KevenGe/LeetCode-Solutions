from typing import List
import unittest


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in range(len(s)):
            if count < len(g) and s[i] >= g[count]:
                count += 1
        return count


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.so = Solution()
        return super().setUp()

    def test_1(self):
        self.assertEqual(self.so.findContentChildren(
            [10, 9, 8, 7], [5, 6, 7, 8]), 2)
        self.assertEqual(self.so.findContentChildren(
            [10, 9, 8, 7], []), 0)
