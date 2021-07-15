# 740. 删除并获得点数
# https://leetcode-cn.com/problems/delete-and-earn/

from typing import List
import collections


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cou = collections.Counter(nums)
        dp = [0] * 10002

        dp[0] = cou[0] * 0
        dp[1] = cou[1] * 1

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + cou[i] * i, dp[i - 1])
        return dp[10000]


if __name__ == "__main__":
    so = Solution()

