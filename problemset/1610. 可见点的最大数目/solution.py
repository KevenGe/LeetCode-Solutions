# 1610. 可见点的最大数目
# https://leetcode-cn.com/problems/maximum-number-of-visible-points/

from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        same_point_num = 0
        point_angles = []
        for point in points:
            if point == location:
                same_point_num += 1
            else:
                point_angles.append(math.atan2(point[1] - location[1], point[0] - location[0]))
        point_angles.sort()
        point_angles += list(map(lambda x: x + 2 * math.pi, point_angles))
        angle = angle * (math.pi / 180)

        ans = 0
        right = 0
        for left in range(int(len(point_angles) / 2)):
            while point_angles[left] + angle >= point_angles[right]:
                right += 1
            ans = max(ans, right - left)

        return ans + same_point_num


if __name__ == "__main__":
    solution = Solution()
    print(solution.visiblePoints([[0, 0], [0, 2]], 90, [1, 1]))
