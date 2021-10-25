# 240. 搜索二维矩阵 II
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/


################################################################################
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = 0
        y = len(matrix[0]) - 1

        while all([x < len(matrix), y >= 0]):
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        
        return False


################################################################################

if __name__ == "__main__":
    solution = Solution()
