from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7

        dp = [[0] * 51 for _ in range(n)]
        for v in range(nums[0] + 1):
            dp[0][v] = 1

        for i in range(1, n):
            for v in range(nums[i] + 1):
                for z in range(v + 1):
                    if nums[i - 1] - z >= nums[i] - v:
                        dp[i][v] = (dp[i][v] + dp[i - 1][z]) % MOD

        return sum(dp[n - 1]) % MOD
