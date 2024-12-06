from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        white_car_x = -1
        white_car_y = -1

        for row_idx, row in enumerate(board):
            for col_idx, x in enumerate(row):
                if x == "R":
                    white_car_x = row_idx
                    white_car_y = col_idx

        ans = 0
        # up
        for d in range(1, 8):
            if white_car_x - d < 0:
                break
            if board[white_car_x - d][white_car_y] == "B":
                break
            elif board[white_car_x - d][white_car_y] == "p":
                ans += 1
                break

        # down
        for d in range(1, 8):
            if white_car_x + d >= 8:
                break
            if board[white_car_x + d][white_car_y] == "B":
                break
            elif board[white_car_x + d][white_car_y] == "p":
                ans += 1
                break

        # left
        for d in range(1, 8):
            if white_car_y - d < 0:
                break
            if board[white_car_x][white_car_y - d] == "B":
                break
            elif board[white_car_x][white_car_y - d] == "p":
                ans += 1
                break

        # right
        for d in range(1, 8):
            if white_car_y + d >= 8:
                break
            if board[white_car_x][white_car_y + d] == "B":
                break
            elif board[white_car_x][white_car_y + d] == "p":
                ans += 1
                break

        return ans
