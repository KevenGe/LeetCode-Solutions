# 80. 删除有序数组中的重复项 II
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 1, -1):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.pop(i)
        return len(nums)
