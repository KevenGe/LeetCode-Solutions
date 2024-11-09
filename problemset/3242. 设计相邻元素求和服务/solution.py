from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

        self.re_map = dict()
        for row_idx, row in enumerate(self.grid):
            for col_idx, x in enumerate(row):
                self.re_map[x] = (row_idx, col_idx)

    def adjacentSum(self, value: int) -> int:
        row_idx, col_idx = self.re_map[value]
        ans = 0
        ans += self.grid[row_idx - 1][col_idx] if row_idx != 0 else 0
        ans += self.grid[row_idx + 1][col_idx] if row_idx != len(self.grid) - 1 else 0
        ans += self.grid[row_idx][col_idx - 1] if col_idx != 0 else 0
        ans += (
            self.grid[row_idx][col_idx + 1] if col_idx != len(self.grid[0]) - 1 else 0
        )
        return ans

    def diagonalSum(self, value: int) -> int:
        row_idx, col_idx = self.re_map[value]
        ans = 0
        ans += (
            self.grid[row_idx - 1][col_idx - 1] if row_idx != 0 and col_idx != 0 else 0
        )
        ans += (
            self.grid[row_idx + 1][col_idx - 1]
            if row_idx != len(self.grid) - 1 and col_idx != 0
            else 0
        )
        ans += (
            self.grid[row_idx + 1][col_idx + 1]
            if row_idx != len(self.grid) - 1 and col_idx != len(self.grid[0]) - 1
            else 0
        )
        ans += (
            self.grid[row_idx - 1][col_idx + 1]
            if row_idx != 0 and col_idx != len(self.grid[0]) - 1
            else 0
        )
        return ans


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
