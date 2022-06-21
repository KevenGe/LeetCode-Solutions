# 473. 火柴拼正方形
# https://leetcode.cn/problems/matchsticks-to-square/

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticksTotal = sum(matchsticks)
        if matchsticksTotal % 4 != 0:
            return False

        tLen = matchsticksTotal // 4

        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for i in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if i & (1 << k) == 0:
                    continue

                s1 = i & ~(1 << k)

                if dp[s1] >= 0 and dp[s1] + v <= tLen:
                    dp[i] = (dp[s1] + v) % tLen
                    break

        return dp[-1] == 0


if __name__ == "__main__":
    so = Solution()
    print(so.makesquare([13, 11, 1, 8, 6, 7, 8, 8, 6, 7, 8, 9, 8]))
