# 42. 接雨水
# https://leetcode-cn.com/problems/trapping-rain-water/

################################################################################
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """单调栈法"""
        ans = 0
        stacks = []
        for i in range(len(height)):

            while len(stacks) >= 2 and height[i] > stacks[-1][0]:
                t = stacks.pop()
                wid = i - stacks[-1][1] - 1
                hei = min(stacks[-1][0], height[i]) - t[0]
                ans += wid * hei

            if len(stacks) == 1 and height[i] > stacks[-1][0]:
                stacks.pop()
            stacks.append((height[i], i))

        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

