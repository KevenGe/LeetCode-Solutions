from typing import List


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0 for i in range(arrLen)]
        dp[0] = 1

        for j in range(steps):
            dpBefore = dp
            dp = [0 for i in range(arrLen)]
            for i in range(j + 1):
                dp[i] = dpBefore[i]
                if i - 1 >= 0:
                    dp[i] += dpBefore[i - 1]
                if i + 1 < arrLen:
                    dp[i] += dpBefore[i + 1]

        return dp[0]