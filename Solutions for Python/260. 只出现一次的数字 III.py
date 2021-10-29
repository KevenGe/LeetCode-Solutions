# 260. 只出现一次的数字 III
# https://leetcode-cn.com/problems/single-number-iii/

################################################################################
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xornum = reduce(lambda x, y: x ^ y, nums, 0)

        t = xornum & -xornum

        t1 = 0
        t2 = 0
        for num in nums:
            if num & t:
                t1 = t1 ^ num
            else:
                t2 = t2 ^ num

        return [t1, t2]


################################################################################

if __name__ == "__main__":
    solution = Solution()
