# 502. IPO
# https://leetcode-cn.com/problems/ipo/

from typing import List
from functools import cmp_to_key
import heapq

class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        dp = [(capital[i], profits[i]) for i in range(len(profits))]
        dp.sort(key=lambda x:x[0])
        dpMax = []
        beforeStart = 0
        for j in range(k):
            while beforeStart < len(dp) and dp[beforeStart][0] <= w:
                heapq.heappush(dpMax, -dp[beforeStart][1])
                beforeStart  += 1

            if len(dpMax) == 0:
                break
            w += -dpMax[0]
            heapq.heappop(dpMax)

        return w



if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 1]))
