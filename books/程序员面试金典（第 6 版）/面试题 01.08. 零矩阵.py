# 面试题 01.08. 零矩阵
# https://leetcode-cn.com/problems/zero-matrix-lcci/

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column_set = set()
        row_set = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    column_set.add(i)
                    row_set.add(j)

        for column_i in column_set:
            for j in range(len(matrix[0])):
                matrix[column_i][j] = 0
        for row_i in row_set:
            for j in range(len(matrix)):
                matrix[j][row_i] = 0

