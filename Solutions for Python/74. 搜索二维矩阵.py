# 74. 搜索二维矩阵
# https://leetcode-cn.com/problems/search-a-2d-matrix/

from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect.bisect_right(list(map(lambda x: x[0], matrix)), target)
        if i == 0:
            return False

        j = bisect.bisect_left(matrix[i - 1], target)
        if j == len(matrix[0]):
            return False
        return matrix[i - 1][j] == target


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1]], 2))
