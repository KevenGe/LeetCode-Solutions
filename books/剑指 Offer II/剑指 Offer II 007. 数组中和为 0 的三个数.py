# 剑指 Offer II 007. 数组中和为 0 的三个数
# https://leetcode.cn/problems/1fGaJU/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans: List[List[int]] = []
        m = 0
        while m < len(nums) - 2:

            t = -nums[m]
            l = m + 1
            r = len(nums) - 1

            while l < r:
                n = nums[l] + nums[r]

                if n == t:
                    ans.append([nums[m], nums[l], nums[r]])
                    while l < r:
                        r -= 1
                        if nums[r] != nums[r + 1]:
                            break
                elif n > t:
                    while l < r:
                        r -= 1
                        if nums[r] != nums[r + 1]:
                            break

                elif n < t:
                    while l < r:
                        l += 1
                        if nums[l] != nums[l - 1]:
                            break

            while m < len(nums) - 2:
                m += 1
                if nums[m] != nums[m - 1]:
                    break

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.threeSum([3, 0, -2, -1, 1, 2]))
