# 319. 灯泡开关
# https://leetcode-cn.com/problems/bulb-switcher/

################################################################################
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


################################################################################

if __name__ == "__main__":
    solution = Solution()
