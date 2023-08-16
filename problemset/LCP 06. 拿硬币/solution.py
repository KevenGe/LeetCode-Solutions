# LCP 06. 拿硬币
# https://leetcode-cn.com/problems/na-ying-bi/

from typing import List
from functools import reduce


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return reduce(lambda x, y: x + (y + 1) // 2, coins, 0)


if __name__ == "__main__":
    solution = Solution()
