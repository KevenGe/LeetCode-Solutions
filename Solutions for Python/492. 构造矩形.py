# 492. 构造矩形
# https://leetcode-cn.com/problems/construct-the-rectangle/

################################################################################
from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        s = math.floor(math.sqrt(area))

        for i in range(s, -1, -1):
            t = area % i
            if t == 0:
                return [area // i, i]


################################################################################

if __name__ == "__main__":
    solution = Solution()
