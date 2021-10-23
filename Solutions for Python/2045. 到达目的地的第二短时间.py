# 2045. 到达目的地的第二短时间
# https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination/

from typing import List
from queue import Queue


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:

        edgs = []
        for i in range(n):
            edgs.append([])
        for a, b in edges:
            edgs[a - 1].append(b)
            edgs[b - 1].append(a)

        dis = [float("inf")] * n
        dis[0] = 0

        que = Queue()
        que.put(1)

        foundTheBest = False

        spendTime = 0

        while que.empty() == False:
            if (spendTime // change) % 2 == 1:
                spendTime = ((spendTime // change) + 1) * change

            spendTime += time

            nextQueSet = set()
            for i in range(que.qsize()):
                s = que.get()
                for j in range(len(edgs[s - 1])):
                    if edgs[s - 1][j] == n:
                        if foundTheBest:
                            return spendTime
                        else:
                            foundTheBest = True
                    nextQueSet.add(edgs[s - 1][j])

            nextQue = Queue()
            for t in nextQueSet:
                nextQue.put(t)
            que = nextQue

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.secondMinimum(2, [[1, 2]], 3, 2))

