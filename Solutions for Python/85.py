from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
