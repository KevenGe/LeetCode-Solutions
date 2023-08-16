# 524. 通过删除字母匹配到字典里最长单词
# https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/

################################################################################
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dp = [[-1 for i in range(26)] for j in range(len(s) + 2)]

        for i in range(len(s) - 1, -1, -1):
            for j in range(26):
                if ord(s[i]) - ord("a") == j:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]

        ans = ""

        for di in dictionary:

            ss = 0
            isGood = True
            for ti in range(len(di)):
                t = dp[ss][ord(di[ti]) - ord("a")]
                if t != -1:
                    ss = t + 1
                else:
                    isGood = False
                    break

            if isGood:
                if len(di) > len(ans) or (len(di) == len(ans) and di < ans):
                    ans = di

        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLongestWord("abpcplea", ["a","b","c"]))

