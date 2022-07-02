# 871. 最低加油次数
# https://leetcode.cn/problems/minimum-number-of-refueling-stops/


from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel

        for i in range(1, len(dp)):
            for j in range(i - 1, -1, -1):
                if dp[j] >= stations[i - 1][0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i - 1][1])

        ans = -1
        for i in range(len(dp)):
            if dp[i] >= target:
                ans = i
                break

        return ans


class TestSolution:
    def test_1(self):
        pass
