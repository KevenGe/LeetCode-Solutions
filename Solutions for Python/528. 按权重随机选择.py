# 528. 按权重随机选择
# https://leetcode-cn.com/problems/random-pick-with-weight/

from typing import List
import random
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self.dp = [0] * len(w)
        self.count = 0
        for i in range(len(w)):
            self.count += w[i]
            self.dp[i] = self.count

    def pickIndex(self) -> int:
        t = random.randint(0, self.count - 1)
        t2 = bisect.bisect(self.dp, t)
        return t2


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
