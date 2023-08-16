# 807. 保持城市天际线
# https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/


################################################################################


from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = [max(grid[i]) for i in range(len(grid))]
        colMax = [
            max([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))
        ]

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(rowMax[i], colMax[j]) - grid[i][j]

        return ans


################################################################################

if __name__ == "__main__":
    so = Solution()
    print(
        so.maxIncreaseKeepingSkyline(
            [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
        )
    )

