# 2089. 找出数组排序后的目标下标
# https://leetcode.cn/problems/find-target-indices-after-sorting-array/

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        ans = []
        if nums[left] == target:
            for idx in range(left, len(nums)):
                if nums[idx] == target:
                    ans.append(idx)
                else:
                    break
        return ans
