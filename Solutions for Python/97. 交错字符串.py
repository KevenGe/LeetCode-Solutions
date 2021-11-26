# 97. 交错字符串
# https://leetcode-cn.com/problems/interleaving-string/

################################################################################
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for s2i in range(len(s2) + 1)] for s1i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, len(s2) + 1):
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]

        for s1i in range(1, len(s1) + 1):
            for s2i in range(1, len(s2) + 1):
                if s1[s1i - 1] == s3[s1i + s2i - 1]:
                    if dp[s1i - 1][s2i]:
                        dp[s1i][s2i] = True
                if s2[s2i - 1] == s3[s1i + s2i - 1]:
                    if dp[s1i][s2i - 1]:
                        dp[s1i][s2i] = True

        return dp[len(s1)][len(s2)]


################################################################################

if __name__ == '__main__':
    solution = Solution()
    print(solution.isInterleave(
        "aa",
        "db",
        "aadb"))
