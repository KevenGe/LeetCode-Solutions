from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ans: List[List[int]] = [[0 for j in range(n - 2)] for i in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                ans[i][j] = max(
                    grid[i][j],
                    grid[i][j + 1],
                    grid[i][j + 2],
                    grid[i + 1][j],
                    grid[i + 1][j + 1],
                    grid[i + 1][j + 2],
                    grid[i + 2][j],
                    grid[i + 2][j + 1],
                    grid[i + 2][j + 2],
                )

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
    print(
        so.largestLocal(
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ]
        )
    )

