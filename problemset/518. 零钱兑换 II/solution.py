from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin] + 1

        return dp[amount]


if __name__ == "__main__":
    so = Solution()
    print(so.change(5, [1, 2, 5]))
