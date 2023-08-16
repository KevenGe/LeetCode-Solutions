# 1221. 分割平衡字符串
# https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/

################################################################################


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dp = [0] * len(s)
        dp[0] = 1 if s[0] == "L" else -1

        ans = 0
        for i in range(1, len(s)):
            dp[i] = dp[i - 1] + (1 if s[i] == "L" else -1)
            if dp[i] == 0:
                ans += 1
        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
