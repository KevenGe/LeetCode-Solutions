# 1219. 黄金矿工
# https://leetcode-cn.com/problems/path-with-maximum-gold/

from typing import List
import copy


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j, gold) -> int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] <= 0:
                return gold

            gold += grid[i][j]
            grid[i][j] = -grid[i][j]

            m = max([dfs(grid, i + 1, j, gold),
                     dfs(grid, i - 1, j, gold),
                     dfs(grid, i, j + 1, gold),
                     dfs(grid, i, j - 1, gold)])
            grid[i][j] = -grid[i][j]
            return m

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                newGrid = copy.deepcopy(grid)
                t = dfs(newGrid, i, j, 0)
                ans = max(ans, t)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.getMaximumGold(
        [[1, 0, 7, 0, 0, 0],
         [2, 0, 6, 0, 1, 0],
         [3, 5, 6, 7, 4, 2],
         [4, 3, 1, 0, 2, 0],
         [3, 0, 5, 0, 20, 0]]
    ))
