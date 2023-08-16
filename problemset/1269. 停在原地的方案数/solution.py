from typing import List


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0] * arrLen
        dp[0] = 1

        t = 10 ** 9 + 7

        for j in range(steps):
            dpBefore = dp
            dp = [0] * (j + 3)
            for i in range(j + 2):
                if i < arrLen:
                    dp[i] = dpBefore[i]
                    if i - 1 >= 0:
                        dp[i] = (dp[i] + dpBefore[i - 1]) % (t)
                    if i + 1 < arrLen:
                        dp[i] = (dp[i] + dpBefore[i + 1]) % (t)
        return dp[0]


if __name__ == "__main__":
    so = Solution()
    print(so.numWays(2, 4))
