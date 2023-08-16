# 1020. 飞地的数量
# https://leetcode-cn.com/problems/number-of-enclaves/

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)

        for j in range(len(grid[0])):
            dfs(grid, 0, j)
            dfs(grid, len(grid) - 1, j)

        for i in range(len(grid)):
            dfs(grid, i, 0)
            dfs(grid, i, len(grid[0]) - 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 1
        return ans
