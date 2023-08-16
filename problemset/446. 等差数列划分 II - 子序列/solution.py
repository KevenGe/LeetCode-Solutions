# 446. 等差数列划分 II - 子序列
# https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/
from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for i in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d = nums[j] - nums[i]
                dp[j][d] += dp[i][d] + 1
                ans += dp[i][d]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfArithmeticSlices([7, 7, 7, 7, 7]))

