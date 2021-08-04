# 264. 丑数 II
# https://leetcode-cn.com/problems/ugly-number-ii/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(1, n):
            t = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if t == dp[p2] * 2:
                p2 += 1
            if t == dp[p3] * 3:
                p3 += 1
            if t == dp[p5] * 5:
                p5 += 1
            dp[i] = t
        return dp[n-1]


if __name__ == "__main__":
    solution = Solution()
