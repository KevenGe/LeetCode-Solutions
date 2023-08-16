# 1450. 在既定时间做作业的学生人数
# https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/

from functools import reduce
from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:

        ans = 0
        for student_id in range(len(startTime)):
            if startTime[student_id] <= queryTime <= endTime[student_id]:
                ans += 1
        return ans

        # return sum(map(lambda student_id: 1 if startTime[student_id] <= queryTime <= endTime[student_id] else 0, range(len(startTime))))
