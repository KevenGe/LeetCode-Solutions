# 1218. 最长定差子序列
# https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/

################################################################################
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        befDict = {}  # value: index
        dp = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            t = arr[i] - difference
            if t in befDict:
                dp[i] = dp[befDict[t]] + 1
            else:
                dp[i] = 1
            ans = max(ans, dp[i])
            befDict[arr[i]] = i
        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
