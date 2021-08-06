# 剑指 Offer 47. 礼物的最大价值
# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])

        return grid[len(grid) - 1][len(grid[0]) - 1]


if __name__ == "__main__":
    solution = Solution()
