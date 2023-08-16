# 1893. 检查是否区域内所有整数都被覆盖
# https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        
        prefix = 0
        for i in range(1, 51):
            prefix += diff[i]
            if i >= left and i <= right and prefix == 0:
                return False
        return True


#
# 这个题目，开拓的新的思路，查分数组加前缀和的方式
#


if __name__ == "__main__":
    solution = Solution()
