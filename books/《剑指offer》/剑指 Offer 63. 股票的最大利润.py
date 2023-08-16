# 剑指 Offer 63. 股票的最大利润
# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = -1
        ans = 0
        for price in prices:
            if m == -1:
                m = price
            m = min(m, price)
            ans = max(ans, price - m)
        return ans


if __name__ == "__main__":
    solution = Solution()
