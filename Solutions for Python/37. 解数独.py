# 37. 解数独
# https://leetcode.cn/problems/sudoku-solver/


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_next_position(row_id: int, col_id: int):
            if col_id < 8:
                return row_id, col_id + 1
            elif col_id == 8:
                if row_id < 8:
                    return row_id + 1, 0
            return -1, -1

        def is_valid(board, row_id, col_id, elm):

            # row
            for i in range(9):
                if board[row_id][i] == elm:
                    return False

            # col
            for i in range(9):
                if board[i][col_id] == elm:
                    return False

            # box
            row_bid = row_id // 3
            col_bid = col_id // 3
            for i in range(row_bid * 3, row_bid * 3 + 3):
                for j in range(col_bid * 3, col_bid * 3 + 3):
                    if board[i][j] == elm:
                        return False

            return True

        def dfs(board: List[List[str]], row_id, col_id) -> bool:
            if row_id == -1 and col_id == -1:
                return True

            if board[row_id][col_id] != ".":
                return dfs(board, *get_next_position(row_id, col_id))

            for i in range(1, 10):
                if is_valid(board, row_id, col_id, str(i)):
                    board[row_id][col_id] = str(i)
                    if dfs(board, *get_next_position(row_id, col_id)):
                        return True
                    board[row_id][col_id] = "."

            return False

        dfs(board, 0, 0)
