# 561. 数组拆分 I
# https://leetcode.cn/problems/array-partition-i/

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) // 2):
            ans += nums[i*2]
        return ans
