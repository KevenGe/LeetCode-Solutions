# 1337. 矩阵中战斗力最弱的 K 行
# https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/

from typing import List
import functools


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dp = []
        for i in range(len(mat)):
            t = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    t += 1
                else:
                    break
            dp.append((t, i))

        def ccc(a, b):
            if a[0] == b[0]:
                return a[1] - b[1]
            else:
                return a[0] - b[0]

        dp.sort(key=functools.cmp_to_key(ccc))
        # print(dp)

        ans = []
        for i in range(k):
            ans.append(dp[i][1])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.kWeakestRows(
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            3,
        )
    )
