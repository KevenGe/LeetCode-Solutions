# 673. 最长递增子序列的个数
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

################################################################################
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # DP ????
        dp = [1] * len(nums)
        cnt = [1] * len(nums)

        dp[0] = 1
        cnt[0] = 1

        maxDp = 1
        maxDpCnt = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                    elif dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]

            if dp[i] > maxDp:
                maxDp = dp[i]
                maxDpCnt = cnt[i]
            elif dp[i] == maxDp:
                maxDpCnt += cnt[i]

        return maxDpCnt


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))

