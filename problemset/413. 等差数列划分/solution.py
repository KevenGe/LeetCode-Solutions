# 413. 等差数列划分
# https://leetcode-cn.com/problems/arithmetic-slices/
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        d = nums[1] - nums[0]
        tn = 0

        ans = 0
        for i in range(2, len(nums)):
            t = nums[i] - nums[i - 1]
            if d == t:
                tn += 1
            else:
                d = t
                tn = 0
            ans += tn

        return ans


if __name__ == "__main__":
    solution = Solution()
