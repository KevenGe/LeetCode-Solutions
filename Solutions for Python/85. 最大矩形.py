# 85. 最大矩形
# https://leetcode-cn.com/problems/maximal-rectangle/

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0


        left = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix[0])):
            left[0][i] = 1 if matrix[0][i] == "1" else 0
            for j in range(1, len(matrix)):
                if matrix[j][i] == "1":
                    left[j][i] = 1 + left[j - 1][i]

        ans = 0
        for j in range(len(left)):
            ans = max(ans, self.ttt(left[j]))
        return ans

    def ttt(self, lists: List[int]):
        l = lists.copy()
        l = l + [0]
        stacks = [[0, -1]]

        ans = 0

        for i in range(len(l)):
            if stacks[-1][0] < l[i]:
                stacks.append([l[i], i])
            elif stacks[-1][0] == l[i]:
                stacks[-1][1] = i
            else:
                while stacks[-1][0] > l[i]:
                    t = stacks.pop()
                    ans = max(ans, (i - stacks[-1][1] - 1) * t[0])
                stacks.append([l[i], i])
        return ans


if __name__ == "__main__":
    solution = Solution()
    t = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # print(solution.maximalRectangle(t))
    print(t[0:1, 0])