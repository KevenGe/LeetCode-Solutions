# 剑指 Offer 53 - II. 0～n-1中缺失的数字
# https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] != m:
                r = m - 1
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    solution = Solution()
