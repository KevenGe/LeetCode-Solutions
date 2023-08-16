# 540. 有序数组中的单一元素
# https://leetcode-cn.com/problems/single-element-in-a-sorted-array/


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #  1 1 2 3 3
        #  0 1 2 3 4
        #  0 0 1 1 2

        n = (len(nums) + 1 ) // 2
        l = 0
        r = n - 1

        ans = 0
        while l <= r:
            m = (l+r) // 2
            if ((2 * m + 1) >= len(nums) or ((2 * m + 1) < len(nums) and nums[m*2] != nums[m*2 + 1])) \
                    and (m == 0 or (nums[m*2] != nums[m*2 - 1])):
                ans = nums[m*2]
                break
            if nums[m*2] == nums[m*2 + 1]:
                l = m + 1
            else:
                r = m - 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNonDuplicate([3,3, 7,7,10,10,11]))



