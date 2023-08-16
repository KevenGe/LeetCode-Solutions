# 剑指 Offer II 004. 只出现一次的数字
# https://leetcode.cn/problems/WGki4K/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for c in nums:
            na = ((~a) & b & c) | (a & (~b) & (~c))
            nb = (~a) & (b ^ c)

            a = na
            b = nb

        return b


if __name__ == "__main__":
    so = Solution()
    print(so.singleNumber([2, 2, 3, 2]))
