# 575. 分糖果
# https://leetcode-cn.com/problems/distribute-candies/

################################################################################
from typing import List
from collections import Counter


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.distributeCandies([1, 1, 2, 3]))
