# 503. 下一个更大元素 II
# https://leetcode.cn/problems/next-greater-element-ii/

from typing import List, Tuple


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        s: List[Tuple[int, int]] = []
        ans = [-1] * len(nums)
        for i in range(len(nums) * 2):
            i = i % len(nums)
            while len(s) > 0 and nums[i] > s[-1][0]:
                ans[s.pop()[1]] = nums[i]
            s.append((nums[i], i))

        return ans
