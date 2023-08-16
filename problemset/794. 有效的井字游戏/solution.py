# 794. 有效的井字游戏
# https://leetcode-cn.com/problems/valid-tic-tac-toe-state/


from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        x_num = 0
        o_num = 0

        for bo in board:
            for t in bo:
                if t == "O":
                    o_num += 1
                elif t == "X":
                    x_num += 1

        if not (x_num == o_num or x_num == o_num + 1):
            return False

        def check_win(pat):
            for i in range(3):
                if board[i][0] == pat and board[i][1] == pat and board[i][2] == pat:
                    return True
                if board[0][i] == pat and board[1][i] == pat and board[2][i] == pat:
                    return True
            if board[0][0] == pat and board[1][1] == pat and board[2][2] == pat:
                return True
            if board[2][0] == pat and board[1][1] == pat and board[0][2] == pat:
                return True
            return False

        x_win = check_win('X')
        o_win = check_win('O')

        if x_win and o_win:
            return False

        if x_win and not x_num == o_num + 1:
            return False

        if o_win and not x_num == o_num:
            return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.validTicTacToe( ["XOX", "O O", "XOX"]))
