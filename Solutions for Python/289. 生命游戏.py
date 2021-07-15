from typing import List


class Solution:

    def isAlive(self, cell):
        return cell & 1

    def nextAlive(self, cell):
        return cell | 2

    def nextDied(self, cell):
        return cell | 1
    
    def isNextAlive(self, cell):
        return cell & 2

    def getLiveNum(self, board: List[List[int]], i, j):
        """
        获取细胞周围的活细胞
        """
        count = 0
        top = True if i - 1 >= 0 else False
        bottom = True if i + 1 < len(board) else False
        left = True if j - 1 >= 0 else False
        right = True if j + 1 < len(board[0]) else False

        if top:
            count += self.isAlive(board[i-1][j])
            if left:
                count += self.isAlive(board[i-1][j-1])
            if right:
                count += self.isAlive(board[i-1][j+1])

        if bottom:
            count += self.isAlive(board[i+1][j])
            if left:
                count += self.isAlive(board[i+1][j-1])

            if right:
                count += self.isAlive(board[i+1][j+1])

        if left:
            count += self.isAlive(board[i][j-1])

        if right:
            count += self.isAlive(board[i][j+1])

        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = self.getLiveNum(board, i, j)
                if self.isAlive(board[i][j]):
                    if n < 2 or n > 3:
                        board[i][j] = self.nextDied(board[i][j])
                    else:
                        board[i][j] = self.nextAlive(board[i][j])
                else:
                    if n == 3:
                        board[i][j] = self.nextAlive(board[i][j])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.isNextAlive(board[i][j]):
                    board[i][j] = 1
                else:
                    board[i][j] = 0


def runTest():
    so = Solution()
    a = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    so.gameOfLife(a)
    print(a)

runTest()

