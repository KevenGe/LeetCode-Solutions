from typing import List
import unittest

# 二分查找
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = 0
#         l = 1
#         r = len(nums) - 1
#         ans = 0
#         while l <= r:
#             m = (l+r) // 2
#             cnt = 0
#             for j in range(0, len(nums)):
#                 cnt += 1 if nums[j] <= m else 0

#             if cnt <= m:
#                 l = m + 1
#             else:
#                 r = m - 1
#                 ans = m
#         return ans

# 快慢指针


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 0
        fast = 0
        while True:
            fast = nums[fast]
            fast = nums[fast]
            low = nums[low]
            if fast == low:
                break
        p1 = 0
        p2 = fast
        while True:
            p1 = nums[p1]
            p2 = nums[p2]
            if p1 == p2:
                return p1
        


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.so  = Solution()

    def test_1(self):
        self.assertEqual(2, self.so.findDuplicate([1, 3, 4, 2, 2]))
        self.assertEqual(3, self.so.findDuplicate([3, 1, 3, 4, 2]))


if __name__ == "__main__":
    unittest.main()
