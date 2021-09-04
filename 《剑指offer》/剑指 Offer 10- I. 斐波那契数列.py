# 剑指 Offer 10- I. 斐波那契数列
# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            m = 1000000007
            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = (dp[i - 2] + dp[i - 1]) % m
            return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(3))
