# 84. 柱状图中最大的矩形
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
# 单调栈解法

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        ans = 0
        sta = [[0, -1]]
        for i, height in enumerate(heights):
            if sta[-1][0] < height:
                sta.append([height, i])
            elif sta[-1][0] == height:
                sta[-1][1] = i
            else:
                while sta[-1][0] > height:
                    h, i2 = sta.pop()
                    ans = max(ans, (i - sta[-1][1] - 1) * h)
                sta.append([height, i])

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([0]))

