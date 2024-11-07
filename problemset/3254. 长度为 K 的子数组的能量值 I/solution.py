from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1

        ans = []
        for i in range(k - 1, n):
            if dp[i] >= k:
                ans.append(nums[i])
            else:
                ans.append(-1)

        return ans
