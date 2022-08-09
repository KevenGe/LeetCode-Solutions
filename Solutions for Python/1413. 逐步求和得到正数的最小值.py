# 1413. 逐步求和得到正数的最小值
# https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/

from typing import List
import itertools


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1 - min(itertools.accumulate(nums)), 0)


if __name__ == "__main__":
    so = Solution()
    print(so.minStartValue([-3, 2, -3, 4, 2]))
