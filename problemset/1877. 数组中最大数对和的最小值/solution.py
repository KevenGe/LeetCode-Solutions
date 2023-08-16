# 1877. 数组中最大数对和的最小值
# https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[len(nums) - i - 1])
        return ans


if __name__ == "__main__":
    solution = Solution()
