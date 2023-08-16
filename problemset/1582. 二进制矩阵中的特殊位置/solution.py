# 1582. 二进制矩阵中的特殊位置
# https://leetcode.cn/problems/special-positions-in-a-binary-matrix/

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_one_nums = [0] * len(mat)
        col_one_nums = [0] * len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row_one_nums[i] += 1

        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i] == 1:
                    col_one_nums[i] += 1

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_one_nums[i] == 1 and col_one_nums[j] == 1:
                    ans += 1
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
    print(so.numSpecial([
        [0, 0, 1, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 1, 0, 0]]))

