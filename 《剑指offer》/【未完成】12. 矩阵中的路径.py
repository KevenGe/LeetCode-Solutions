from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or word == 0:
            return False

        def search(i, j):
            dp = [[False for i_ in range(len(board[0]))] for j_ in range(len(board))]
            wordHasLen = 0
            isFound = False

            def dfs(i, j):
                """"""
                global wordHasLen, isFound
                if isFound is True:
                    return
                if wordHasLen == len(word):
                    isFound = True
                    return

                if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                    if dp[i][j] is False and dp[i][j] == word[wordHasLen]:
                        dp[i][j] = True
                        wordHasLen += 1
                        dfs(i + 1, j)
                        dfs(i - 1, j)
                        dfs(i, j + 1)
                        dfs(i, j - 1)
                        wordHasLen -= 1
                        dp[i][j] = False

            dfs(i, j)
            return isFound

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i, j):
                        return True

        return False
