from itertools import product
from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        one_one_count = 0
        one_zero_count = 0
        for i, j in product(range((m + 1) // 2), range((n + 1) // 2)):

            if i == m - 1 - i and j == n - 1 - j:
                if grid[i][j] == 1:
                    ans += 1
                    break

            if i == m - 1 - i:
                vs = [grid[i][j], grid[i][n - 1 - j]]
                one_count = sum(vs)
                zero_cont = 2 - one_count

                if one_count == 0:
                    ans += 0
                elif one_count == 1:
                    ans += 1
                    one_zero_count += 1
                else:
                    ans += 0
                    one_one_count += 2

                continue

            if j == n - 1 - j:
                vs = [grid[i][j], grid[m - 1 - i][j]]
                one_count = sum(vs)
                zero_cont = 2 - one_count

                if one_count == 0:
                    ans += 0
                elif one_count == 1:
                    ans += 1
                    one_zero_count += 1
                else:
                    ans += 0
                    one_one_count += 2

                continue

            one_count = sum(
                [
                    grid[i][j],
                    grid[i][n - 1 - j],
                    grid[m - 1 - i][j],
                    grid[m - 1 - i][n - 1 - j],
                ]
            )
            ans += min(one_count, 4 - one_count)

        if one_one_count % 4 != 0 and one_zero_count == 0:
            ans += 2

        return ans
