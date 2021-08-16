# 剑指 Offer 59 - I. 滑动窗口的最大值
# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        leftMax = [0] * len(nums)
        rightMax = [0] * len(nums)

        for i in range(len(nums)):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])

        for i in range(len(nums) - 1, -1, -1):
            if (i + 1) % k == 0 or i == len(nums) - 1:
                rightMax[i] = nums[i]
            else:
                rightMax[i] = max(rightMax[i + 1], nums[i])

        ans = []
        for r in range(k - 1, len(nums)):
            t = max(leftMax[r], rightMax[r - k + 1])
            ans.append(t)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

