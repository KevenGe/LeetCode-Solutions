# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/

################################################################################


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        for i in range(len(s)):
            if s[i] != "0":
                dp[i + 1] += dp[i]
            if i >= 1 and s[i - 1] != "0" and int(s[i - 1 : i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[len(dp) - 1]


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings("06"))
