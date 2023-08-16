# 268. 丢失的数字
# https://leetcode-cn.com/problems/missing-number/

################################################################################
# from typing import List
# from functools import reduce


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         t = reduce(lambda x, y: x ^ y, list(range(len(nums) + 1)), 0)
#         ans = reduce(lambda x, y: x ^ y, nums, t)
#         return ans


################################################################################
from typing import List
from functools import reduce


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t = reduce(lambda x, y: x + y, list(range(len(nums) + 1)), 0)
        ans = reduce(lambda x, y: x - y, nums, t)
        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
