# 1646. 获取生成数组中的最大值
# https://leetcode-cn.com/problems/get-maximum-in-generated-array/


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(n + 1):
            if 2 <= 2 * i <= n:
                dp[2 * i] = max(dp[2*i], dp[i])
            if 2 <= 2 * i + 1 <= n:
                dp[2 * i + 1] = max(dp[2 * i + 1], dp[i] + dp[i + 1])

        ans = max(dp)
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.getMaximumGenerated(11))
