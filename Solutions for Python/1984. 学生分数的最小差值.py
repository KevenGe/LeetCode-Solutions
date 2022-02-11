# 1984. 学生分数的最小差值
# https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minSub = 10000000
        for i in range(len(nums) - k + 1):
            if nums[i + k - 1] - nums[i] < minSub:
                minSub = nums[i + k - 1] - nums[i]
        return minSub
