# LCP 06. 拿硬币
# https://leetcode-cn.com/problems/na-ying-bi/

from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        count = 0
        for coin in coins:
            count += (coin + 1) // 2
        return count


if __name__ == "__main__":
    solution = Solution()
