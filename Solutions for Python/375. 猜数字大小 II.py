# 375. 猜数字大小 II
# https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/

################################################################################


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = float("inf")
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))

        return dp[1][n]


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.getMoneyAmount(10))
