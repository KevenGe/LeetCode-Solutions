# LCP 07. 传递信息
# https://leetcode-cn.com/problems/chuan-di-xin-xi/

from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:

        tar = {}
        for rel in relation:
            if rel[0] not in tar:
                tar[rel[0]] = [rel[1]]
            else:
                tar[rel[0]].append(rel[1])

        dp = [[0 for i in range(n)] for j in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            for j in range(n):
                if dp[i - 1][j] > 0 and j in tar:
                    for t in tar[j]:
                        dp[i][t] += dp[i - 1][j]

        return dp[k][n-1]


if __name__ == "__main__":
    solution = Solution()
