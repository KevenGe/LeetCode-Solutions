# 2006. 差的绝对值为 K 的数对数目
# https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k/

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        passed_nums = {}

        ans = 0
        for num in nums:
            if num + k in passed_nums:
                ans += passed_nums[num + k]

            if num - k in passed_nums:
                ans += passed_nums[num - k]

            if num in passed_nums:
                passed_nums[num] += 1
            else:
                passed_nums[num] = 1

        return ans