# 704. 二分查找
# https://leetcode-cn.com/problems/binary-search/

################################################################################

# from typing import List
# import bisect


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         t = bisect.bisect_left(nums, target)
#         if t >= len(nums) or t < 0 or nums[t] != target:
#             return -1
#         return t


################################################################################

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1


################################################################################


if __name__ == "__main__":
    solution = Solution()
