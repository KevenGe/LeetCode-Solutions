# 212. 单词搜索 II
# https://leetcode-cn.com/problems/word-search-ii/


################################################################################
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTree = {}
        for word in words:
            t = wordTree
            for s in word:
                if s not in t:
                    t[s] = {}
                t = t[s]
            t["end"] = None

        def dfs(bd, t, i, j, tmpWord, ans):
            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return

            tmp = board[i][j]

            if tmp in t:

                t2 = t[tmp]

                tmpWord += bd[i][j]

                if "end" in t2:
                    ans.add(tmpWord)

                t3 = bd[i][j]
                bd[i][j] = "#"
                dfs(bd, t2, i + 1, j, tmpWord, ans)
                dfs(bd, t2, i - 1, j, tmpWord, ans)
                dfs(bd, t2, i, j + 1, tmpWord, ans)
                dfs(bd, t2, i, j - 1, tmpWord, ans)
                bd[i][j] = t3
            else:
                return

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, wordTree, i, j, "", ans)
        return list(ans)


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findWords(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        )
    )

