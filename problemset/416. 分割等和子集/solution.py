from typing import List
import unittest


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        # 不可以是奇数
        if s % 2 == 1:
            return False

        # 目标
        s = s // 2
        dp = [False for _ in range(s + 1)]
        dp[0] = True

        for n in nums:
            for i in reversed(range(len(dp))):
                if i + n <= s and dp[i]:
                    dp[i + n] = True

        return dp[s]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.so = Solution()

    def test1(self):
        self.assertFalse(self.so.canPartition([1, 3, 5]))


def runTest():
    s = Solution()
    print(s.canPartition([2,2,1,1]))

runTest()
