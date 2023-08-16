# 剑指 Offer 53 - I. 在排序数组中查找数字 I
#
from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        ans = 0
        while i < len(nums) and nums[i] == target:
            ans += 1
            i += 1
        return ans


if __name__ == "__main__":
    so = Solution()
