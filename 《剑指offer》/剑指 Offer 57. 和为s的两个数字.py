# 剑指 Offer 57. 和为s的两个数字
# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if target - nums[left] == nums[right]:
                return [nums[left], nums[right]]
            elif target - nums[left] > nums[right]:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    solution = Solution()
