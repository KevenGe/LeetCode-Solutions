# 1218. 最长定差子序列
# https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/

################################################################################
from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = defaultdict(int)
        for i in range(len(arr)):
            dp[arr[i]] = dp[arr[i] - difference] + 1
        return max(dp.values())


################################################################################

if __name__ == "__main__":
    solution = Solution()
