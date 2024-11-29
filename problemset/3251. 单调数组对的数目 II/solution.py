from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7

        dp = [[0] * 1001 for _ in range(n)]
        for v in range(nums[0] + 1):
            dp[0][v] = 1

        for i in range(1, n):
            d = max(0, nums[i] - nums[i - 1])
            for v in range(nums[i] + 1):
                # Old Code
                # for z in range(v + 1):
                #     if nums[i - 1] - z >= nums[i] - v:
                #         dp[i][v] = (dp[i][v] + dp[i - 1][z]) % MOD

                # New Code
                if v == 0:
                    dp[i][v] = dp[i - 1][v - d]
                else:
                    dp[i][v] = (dp[i][v - 1] + dp[i - 1][d]) % MOD

        return sum(dp[n - 1]) % MOD
