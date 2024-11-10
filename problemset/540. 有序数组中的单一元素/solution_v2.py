from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] == nums[m ^ 1]:
                l = m + 1
            else:
                r = m

        return nums[l]
