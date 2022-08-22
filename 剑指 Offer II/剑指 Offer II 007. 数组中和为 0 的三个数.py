# 剑指 Offer II 007. 数组中和为 0 的三个数
# https://leetcode.cn/problems/1fGaJU/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans: List[List[int]] = []
        pm = set()
        for m in range(len(nums) - 2):
            if nums[m] in pm:
                continue

            pm.add(nums[m])

            t = -nums[m]
            l = m + 1
            r = len(nums) - 1
            pl = set()
            pr = set()

            while l < r:
                n = nums[l] + nums[r]

                if n == t:
                    ans.append([nums[m], nums[l], nums[r]])

                    pr.add(nums[r])
                    while l < r:
                        if nums[r] in pr:
                            r -= 1
                        else:
                            break
                elif n > t:
                    pr.add(nums[r])
                    while l < r:
                        if nums[r] in pr:
                            r -= 1
                        else:
                            break
                elif n < t:
                    pl.add(nums[l])
                    while l < r:
                        if nums[l] in pl:
                            l += 1
                        else:
                            break

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.threeSum([3, 0, -2, -1, 1, 2]))
