class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        MOD = int(1e9 + 7)

        dp = [1] * 10
        next = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        for _ in range(1, n):
            next_dp = [0] * 10
            for i in range(10):
                for j in next[i]:
                    next_dp[i] = (next_dp[i] + dp[j]) % MOD
            dp = next_dp

        return sum(dp) % MOD
