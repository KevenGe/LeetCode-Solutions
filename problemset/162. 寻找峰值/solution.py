# 162. 寻找峰值
# https://leetcode-cn.com/problems/find-peak-element/


################################################################################

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1

        l = 1
        r = len(nums) - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                if nums[m] < nums[m - 1]:
                    r = m - 1
                else:
                    return m


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([2, 3, 1]))

