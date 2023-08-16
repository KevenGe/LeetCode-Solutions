# 18. 四数之和
# https://leetcode-cn.com/problems/4sum/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  a + b + c + d = 0

        nums.sort()

        ans: List[List[int]] = []
        ai = 0
        while ai < len(nums):
            a = nums[ai]

            di = ai + 1

            while di < len(nums):
                d = nums[di]

                bi = di + 1
                ci = len(nums) - 1

                while bi < ci:

                    b = nums[bi]
                    c = nums[ci]

                    e = a + b + c + d
                    if e == target:
                        ans.append([a, d, b, c])
                        while ci - 1 > bi and nums[ci] == nums[ci - 1]:
                            ci -= 1
                        ci -= 1
                        while bi + 1 < ci and nums[bi] == nums[bi + 1]:
                            bi += 1
                        bi += 1
                    elif e > target:
                        while ci - 1 > bi and nums[ci] == nums[ci - 1]:
                            ci -= 1
                        ci -= 1
                    elif e < target:
                        while bi + 1 < ci and nums[bi] == nums[bi + 1]:
                            bi += 1
                        bi += 1

                while di + 1 < len(nums) and nums[di] == nums[di + 1]:
                    di += 1
                di += 1


            while ai + 1 < len(nums) and nums[ai] == nums[ai + 1]:
                ai += 1
            ai += 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([1,-2,-5,-4,-3,3,3,5], -11))
