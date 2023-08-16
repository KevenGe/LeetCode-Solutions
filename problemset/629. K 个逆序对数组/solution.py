# 629. K个逆序对数组
# https://leetcode-cn.com/problems/k-inverse-pairs-array/

################################################################################


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        elif n == 1:
            return 0

        m = 10 ** 9 + 7

        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]

        # I == 2
        dp[2][0] = 1
        dp[2][1] = 1

        for i in range(3, n + 1):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % m
                if j - i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i]) % m

        return dp[n][k]


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.kInversePairs(3, 2))
