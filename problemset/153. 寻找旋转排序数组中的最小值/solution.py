# 153.寻找旋转排序数组中的最小值
# https://leetcode.cn/leetbook/read/array-and-string/c3ki5/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]


        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if (m + 1 >= len(nums) or (m + 1 < len(nums) and nums[m] < nums[m+1])) and \
                    (m - 1 <= 0 and (m - 1 > 0 and nums[m] > nums[m-1])):
                return nums[m]
            else:
                if nums[m] < nums[0]:
                    r = m - 1
                else:
                    l = m + 1

        return nums[l]


class TestSolution:
    def test_one(self):
        so = Solution()
        assert so.findMin([1, 2, 3, 4, 5]) == 1, "111"
        assert so.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
        assert so.findMin([11, 13, 15, 17]) == 11

if __name__ == "__main__":
    so = Solution()
    print(so.findMin([1]) == 1)

