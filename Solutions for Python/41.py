from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        inf = float('inf')
        for i in range(len(nums)):
            nums[i] = inf if nums[i] <= 0 else nums[i]

        for i in range(len(nums)):
            n = abs(nums[i])
            if n >= 1 and n <= len(nums):
                nums[n-1] = -abs(nums[n-1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1

        return len(nums) + 1


so = Solution()
print(so.firstMissingPositive([1, 1]))
