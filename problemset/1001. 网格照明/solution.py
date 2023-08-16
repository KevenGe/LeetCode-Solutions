# 1001. 网格照明
# https://leetcode-cn.com/problems/grid-illumination/

from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row = {}
        col = {}
        dig = {}
        anti_dig = {}
        pos = {}

        for x, y in lamps:
            if x in pos:
                pos[x][y] = 1
            else:
                pos[x] = {
                    y: 1
                }

        for k, v in pos.items():
            for k2, v2 in v.items():
                x = k
                y = k2

                if x in row:
                    row[x] += 1
                else:
                    row[x] = 1

                if y in col:
                    col[y] += 1
                else:
                    col[y] = 1

                if y - x in dig:
                    dig[y - x] += 1
                else:
                    dig[y - x] = 1

                if y + x in anti_dig:
                    anti_dig[y + x] += 1
                else:
                    anti_dig[y + x] = 1

        ans = []
        for x, y in queries:
            if (x in row and row[x] > 0) or \
                    (y in col and col[y] > 0) or \
                    (y - x in dig and dig[y - x] > 0) or \
                    (y + x in anti_dig and anti_dig[y + x] > 0):
                ans.append(1)
            else:
                ans.append(0)

            for delta_x in range(-1, 2, 1):
                for delta_y in range(-1, 2, 1):
                    nx = x + delta_x
                    ny = y + delta_y

                    if nx in pos and ny in pos[nx] and pos[nx][ny] == 1:
                        pos[nx][ny] = 0
                        row[nx] -= 1
                        col[ny] -= 1
                        dig[ny - nx] -= 1
                        anti_dig[ny + nx] -= 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.gridIllumination(
        6, [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]],
        [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]
    ))
