from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        maps = [["." for j in range(n)] for i in range(n)]

        ans = []

        def dfs(maps, i, n):
            if i == n:
                pass

            for j in range(len(maps)):

                maps[j] = "Q"
                dfs(maps, i + 1, n)

        dfs(maps, 0, n)
