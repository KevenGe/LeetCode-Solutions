from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def dfs(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs(i + 1, j)
                    dfs(i - 1, j)
                    dfs(i, j + 1)
                    dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


if __name__ == "__main__":
    so = Solution()
    print(
        so.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
    )

