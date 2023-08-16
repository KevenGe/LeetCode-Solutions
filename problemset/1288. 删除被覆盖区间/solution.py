# 1288. 删除被覆盖区间
# https://leetcode-cn.com/problems/remove-covered-intervals/

################################################################################
from typing import List
from functools import cmp_to_key

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        def myCmp(a,b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return b[1] - a[1]

        intervals.sort(key=cmp_to_key(myCmp))
        tmpList = [intervals[-1][1]]
        for i in range(len(intervals) - 1, 0, -1):
            if tmpList[-1] <= intervals[i-1][1]:
                while len(tmpList)!= 0 and tmpList[-1] <= intervals[i-1][1]:
                    tmpList.pop()
                tmpList.append(intervals[i-1][1])
            else:
                tmpList.append(intervals[i-1][1])
        return len(tmpList)

################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeCoveredIntervals([[1,2],[1,4],[3,4]]))
