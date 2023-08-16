# 剑指 Offer 38. 字符串的排列
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans: List[str] = []

        t = s[:]
        t = sorted(list(t))
        ans.append("".join(t))

        while True:
            t = t[:]
            if self.nextPermutation(t) is not None:
                break
            ans.append("".join(t))
        return ans

    def nextPermutation(self, nums) -> None:
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
            # nums.sort()
            return False

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
