MOD = int(1e9 + 7)


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD

                if j > 0:
                    dp[i][j][1] = (
                        (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]) + dp[i - 1][j][1]
                    ) % MOD
                else:
                    dp[i][j][1] = (dp[i - 1][j][1]) % MOD

        return (dp[n - 1][k][0] + dp[n - 1][k][1]) % MOD


################################################################################
# !!! overtime
# !!! overtime
# !!! overtime

# from functools import lru_cache, cache


# MOD = int(1e9 + 7)

# class Solution:

#     @lru_cache(maxsize=1000000)
#     def numberOfSets(self, n: int, k: int) -> int:
#         if n < k or n == 1:
#             return 0

#         if n == k + 1:
#             return 1

#         if k == 1:
#             return n * (n - 1) // 2

#         ans = 0
#         for i in range(1, n):
#             ans = (ans + i * self.numberOfSets(n - i, k - 1)) % MOD
#         return ans
