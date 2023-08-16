# 506. 相对名次
# https://leetcode-cn.com/problems/relative-ranks/

from typing import List
from queue import PriorityQueue


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        a = PriorityQueue()

        for s in score:
            a.put(-s)

        d = {}
        i = 1
        while not a.empty():
            t = a.get()
            if i == 1:
                d[-t] = "Gold Medal"
            elif i == 2:
                d[-t] = "Silver Medal"
            elif i == 3:
                d[-t] = "Bronze Medal"
            else:
                d[-t] = str(i)
            i += 1

        ans = list(map(lambda s:d[s], score))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findRelativeRanks([5,4,3,2,1]))