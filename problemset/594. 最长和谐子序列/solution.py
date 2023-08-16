# 594. 最长和谐子序列
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/

################################################################################
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()

        l = 0
        r = 0
        ans = 0
        while r + 1 < len(nums):

            r = r + 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r = r + 1

            while l < r and nums[l] != nums[r] - 1 and nums[l] != nums[r]:
                l = l + 1

            if nums[l] + 1 == nums[r]:
                ans = max(ans, r - l + 1)
        return ans


################################################################################
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLHS([1, 1, 1, 1]))

