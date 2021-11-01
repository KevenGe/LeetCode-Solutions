# 2045. 到达目的地的第二短时间
# https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination/

################################################################################

from typing import List


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        edgesList = [[] for i in range(n + 1)]
        for s, t in edges:
            edgesList[s].append(t)
            edgesList[t].append(s)

        passedTime = 0  # passed time

        curStacks = set()
        curStacks.add(1)

        visitedTimes = {}

        ans = -1

        while True:

            if (passedTime // change) % 2 == 1:
                passedTime = (passedTime // change + 1) * change
            passedTime += time

            nextStacks = set()
            for s in curStacks:
                if s in visitedTimes:
                    if visitedTimes[s] > 2:
                        continue
                    else:
                        visitedTimes[s] += 1
                else:
                    visitedTimes[s] = 1

                for t in edgesList[s]:
                    if t == n:
                        if ans == -1:
                            ans = -2
                        elif ans == -3:
                            return passedTime
                    nextStacks.add(t)
            if ans == -2:
                ans = -3

            curStacks = nextStacks


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.secondMinimum(5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5))

