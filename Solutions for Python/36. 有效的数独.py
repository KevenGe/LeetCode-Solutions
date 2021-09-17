# 36. 有效的数独
# https://leetcode-cn.com/problems/valid-sudoku/


################################################################################
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row
        for i in range(9):
            t = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in t:
                        return False
                    else:
                        t.add(board[i][j])

        # column
        for i in range(9):
            t = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in t:
                        return False
                    else:
                        t.add(board[j][i])

        # 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                t = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] != ".":
                            if board[m][n] in t:
                                return False
                            else:
                                t.add(board[m][n])

        return True


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )

