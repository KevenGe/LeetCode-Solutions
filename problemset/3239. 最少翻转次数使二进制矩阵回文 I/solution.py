from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        MAX_INT = 9999999
        ans = MAX_INT

        change_count = 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - j - 1]:
                    change_count += 1
        ans = min(ans, change_count)


        change_count = 0
        for i in range(n):
            for j in range(m // 2):
                if grid[j][i] != grid[m - 1 - j][i]:
                    change_count += 1
        ans = min(ans, change_count)

        return ans
