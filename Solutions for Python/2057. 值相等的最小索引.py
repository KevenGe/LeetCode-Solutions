# 2057. 值相等的最小索引
# https://leetcode-cn.com/problems/smallest-index-with-equal-value/

################################################################################
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1


################################################################################

if __name__ == "__main__":
    solution = Solution()
