# 剑指 Offer II 095. 最长公共子序列
# https://leetcode-cn.com/problems/qJnOS7/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1, len(text1)):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, len(text2)):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1) - 1][len(text2) - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonSubsequence("abcde", "abc"))
