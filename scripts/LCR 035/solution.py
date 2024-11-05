from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def get_minute(t: str) -> int:
            return int(t[0:2]) * 60 + int(t[3:5])

        timePoints.sort()

        mins = list(map(get_minute, timePoints))

        ans = 999999999
        for i in range(len(timePoints) - 1):
            ans = min(ans, abs(mins[i] - mins[i + 1]))
        ans = min(ans, abs(mins[0]  + 1440 - mins[len(timePoints) - 1]))

        return ans
