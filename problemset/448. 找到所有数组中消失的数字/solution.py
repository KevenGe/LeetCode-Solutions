from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            pos = abs(nums[i])
            if nums[pos-1] > 0:
                nums[pos-1] = - nums[pos-1]

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)

        return ans
