# 435. 无重叠区间
# https://leetcode.cn/problems/non-overlapping-intervals/

from re import L
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0

        last_right = -9999999999

        for i in range(len(intervals)):
            if intervals[i][0] >= last_right:
                last_right = intervals[i][1]
            else:
                ans += 1

        return ans
