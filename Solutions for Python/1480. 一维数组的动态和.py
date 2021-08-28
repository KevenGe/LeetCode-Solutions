# 1480. 一维数组的动态和
# https://leetcode-cn.com/problems/running-sum-of-1d-array/
from typing import List
from functools import reduce


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        t = 0
        for num in nums:
            t += num
            ans.append(t)

        return ans


if __name__ == "__main__":
    solution = Solution()
