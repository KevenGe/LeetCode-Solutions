# 495. 提莫攻击
# https://leetcode-cn.com/problems/teemo-attacking/

################################################################################
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) ==0:
            return 0

        lastTime = timeSeries[0]
        cou = duration

        for i in range(1, len(timeSeries)):
            if timeSeries[i] < lastTime + duration:
                cou -= lastTime + duration - timeSeries[i]
            cou += duration
            lastTime = timeSeries[i]

        return cou

################################################################################

if __name__ == '__main__':
    solution = Solution()
    print(solution.findPoisonedDuration([1,2,3,4,5], 5))
