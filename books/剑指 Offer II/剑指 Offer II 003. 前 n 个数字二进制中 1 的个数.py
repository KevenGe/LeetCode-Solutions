# 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数
# https://leetcode.cn/problems/w3tCBm/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        high_bit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                high_bit = i
            ans[i] = ans[i - high_bit] + 1
        return ans
