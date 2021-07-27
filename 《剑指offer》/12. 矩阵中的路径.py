# 剑指 Offer 12. 矩阵中的路径
# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or word == 0:
            return False

        def search(i, j, word: str):

            dp = [[False for j in range(len(board[0]))] for i in range(len(board))]

            def f(i, j, word: str, dp):
                if len(word) == 0:
                    return True

                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                    return False

                if dp[i][j] == False and board[i][j] == word[0]:
                    dp[i][j] = True
                    ans = (
                        f(i + 1, j, word[1:], dp)
                        or f(i - 1, j, word[1:], dp)
                        or f(i, j - 1, word[1:], dp)
                        or f(i, j + 1, word[1:], dp)
                    )
                    dp[i][j] = False
                    return ans
                else:
                    return False

            return f(i, j, word, dp)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i, j, word):
                        return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.exist([["a", "a"]], "aaa"))

