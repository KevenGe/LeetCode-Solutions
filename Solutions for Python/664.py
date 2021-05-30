# class Solution:
#     def strangePrinter(self, s: str) -> int:
#         newS = []
#         before = "1"
#         for i in s:
#             if i != before:
#                 newS.append(i)
#                 before = i
#         s = newS

#         n = len(s)

#         dp = [[0 for i in range(n)] for j in range(n)]
#         for i in range(n - 1, -1, -1):
#             dp[i][i] = 1


#             lastIndex = dict([(chr(ord("a")+i), -1) for i in range(26)])

#             lastIndex[s[i]] = i
#             for j in range(i + 1, n):
#                 if lastIndex[s[j]] == -1:
#                     dp[i][j] = dp[i][j - 1] + 1

#                 else:
#                     dp[i][j] = dp[i][lastIndex[s[j]]] + dp[lastIndex[s[j]] + 1][j - 1]
#                 lastIndex[s[j]] = j
#         return dp[0][len(newS) - 1]


# if __name__ == "__main__":
#     so = Solution()
#     print(so.strangePrinter("dddccbdbababaddcbcaabdbdddcccddbbaabddb"))
