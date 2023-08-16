# 1034. 边界着色
# https://leetcode-cn.com/problems/coloring-a-border/


import sys

sys.setrecursionlimit(1000000)
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

        def isEdge(row, col):
            if (row - 1 >= 0 and grid[row - 1][col] != grid[row][col]) \
                    or (row + 1 < len(grid) and grid[row + 1][col] != grid[row][col]) \
                    or (col - 1 >= 0 and grid[row][col - 1] != grid[row][col]) \
                    or (col + 1 < len(grid[0]) and grid[row][col + 1] != grid[row][col]) \
                    or (row == 0) or (col == 0) or (row == len(grid) - 1) or (col == len(grid[0]) - 1):
                return True
            return False

        wait_to_paint = []
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        def dfs(grid, row, col, visited, wait_to_paint):
            if visited[row][col] == 0:
                visited[row][col] = 1
                if isEdge(row, col):
                    wait_to_paint.append([row, col])

                if row - 1 >= 0 and grid[row - 1][col] == grid[row][col]:
                    dfs(grid, row - 1, col, visited, wait_to_paint)

                if row + 1 < len(grid) and grid[row + 1][col] == grid[row][col]:
                    dfs(grid, row + 1, col, visited, wait_to_paint)

                if col - 1 >= 0 and grid[row][col - 1] == grid[row][col]:
                    dfs(grid, row, col - 1, visited, wait_to_paint)

                if col + 1 < len(grid[0]) and grid[row][col + 1] == grid[row][col]:
                    dfs(grid, row, col + 1, visited, wait_to_paint)

        dfs(grid, row, col, visited, wait_to_paint)

        for x, y in wait_to_paint:
            grid[x][y] = color

        return grid


if __name__ == "__main__":
    solution = Solution()
    print(solution.colorBorder([[1, 2, 1, 2, 1, 2],
                                [2, 2, 2, 2, 1, 2],
                                [1, 2, 2, 2, 1, 2]], 1, 3, 1))
