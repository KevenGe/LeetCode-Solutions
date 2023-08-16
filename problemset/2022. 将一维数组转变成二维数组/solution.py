# 2022. 将一维数组转变成二维数组
# https://leetcode-cn.com/problems/convert-1d-array-into-2d-array/

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return [[]]

        ans = [[0 for j in range(n)] for i in range(m)]
        for i,x in enumerate(original):
            mi = i // n
            ni = i % n
            ans[mi][ni] = x
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.construct2DArray([1,2,3], 1,3))
