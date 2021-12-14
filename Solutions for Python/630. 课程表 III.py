# 630. 课程表 III
# https://leetcode-cn.com/problems/course-schedule-iii/


################################################################################


from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        que = []
        total = 0

        for t, d in courses:
            if total + t <= d:
                total += t

                heapq.heappush(que, -t)
            else:
                if len(que) != 0 and -que[0] > t:
                    total = total + que[0] + t
                    heapq.heappop(que)
                    heapq.heappush(que, -t)

        return len(que)

################################################################################
