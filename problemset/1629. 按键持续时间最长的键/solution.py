# 1629. 按键持续时间最长的键
# https://leetcode-cn.com/problems/slowest-key/

from typing import List
from collections import defaultdict


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxK = ""
        maxV = -1
        for i in range(len(keysPressed)):
            keyTime = releaseTimes[i] - (releaseTimes[i - 1] if i - 1 >= 0 else 0)

            k = keysPressed[i]
            v = keyTime
            if v > maxV or (v == maxV and k > maxK):
                maxV = v
                maxK = k

        return maxK

