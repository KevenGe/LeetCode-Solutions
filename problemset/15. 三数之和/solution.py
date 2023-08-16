# 15. 三数之和
# https://leetcode-cn.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  a + b + c = 0

        nums.sort()

        ans: List[List[int]] = []
        ai = 0
        while ai < len(nums):
            a = nums[ai]
            if a > 0:
                break

            bi = ai + 1
            ci = len(nums) - 1

            while bi < ci:

                b = nums[bi]
                c = nums[ci]

                d = a + b + c
                if d == 0:
                    ans.append([a, b, c])
                    while ci - 1 > bi and nums[ci] == nums[ci - 1]:
                        ci -= 1
                    ci -= 1
                    while bi + 1 < ci and nums[bi] == nums[bi + 1]:
                        bi += 1
                    bi += 1
                elif d > 0:
                    while ci - 1 > bi and nums[ci] == nums[ci - 1]:
                        ci -= 1
                    ci -= 1
                elif d < 0:
                    while bi + 1 < ci and nums[bi] == nums[bi + 1]:
                        bi += 1
                    bi += 1

            while ai + 1 < len(nums) and nums[ai] == nums[ai + 1]:
                ai += 1
            ai += 1

        return ans


if __name__ == "__main__":
    pass
