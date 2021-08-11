# 31. 下一个排列
# https://leetcode-cn.com/problems/next-permutation/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if j > 0 and nums[j - 1] < nums[j]:
                l = j - 1
                break
        if l == -1:
            nums.sort()
            return

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > nums[l]:
                r = j
                break

        nums[l], nums[r] = nums[r], nums[l]

        for i in range(l + 1, len(nums) - 1):
            t = len(nums) - 1 - (i - (l + 1))
            if i < t:
                nums[i], nums[t] = nums[t], nums[i]
            else:
                break


if __name__ == "__main__":
    solution = Solution()
    t = [3, 2, 1]
    solution.nextPermutation(t)
    print(t)
