# 485. 最大连续 1 的个数
# https://leetcode.cn/problems/max-consecutive-ones/


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0

        cur_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 0
        return max_len
