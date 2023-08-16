# 1403. 非递增顺序的最小子序列
# https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        ns = 0
        ans = []
        for i, n in enumerate(nums):
            ans.append(n)
            ns += n
            if ns > s - ns:
                break

        return ans
