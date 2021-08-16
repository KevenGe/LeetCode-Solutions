# 剑指 Offer 19. 正则表达式匹配
# https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[0][i] = False
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                if i - 2 >= 0:
                    dp[i][0] = dp[i - 2][0]
                else:
                    dp[i][0] = False

        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == s[j] or p[i] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[i] == "*":
                    if p[i - 1] == ".":
                        dp[i + 1][j + 1] = (
                            dp[i][j + 1] or dp[i + 1][j] or dp[i - 1][j + 1]
                        )
                    else:
                        dp[i + 1][j + 1] = (
                            dp[i - 1][j + 1]
                            or dp[i][j + 1]
                            or (dp[i][j] and p[i - 1] == s[j])
                        )
                else:
                    dp[i + 1][j + 1] = False
        return dp[len(p)][len(s)]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aa", ".*a.*a"))
