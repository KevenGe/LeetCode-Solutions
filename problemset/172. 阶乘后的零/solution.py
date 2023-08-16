# 172. 阶乘后的零
# https://leetcode.cn/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += (n := n // 5)
        return ans
