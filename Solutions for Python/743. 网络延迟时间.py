# 743. 网络延迟时间
# https://leetcode-cn.com/problems/network-delay-time/

from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # getD
        d = {}
        for i in range(1, n + 1):
            d[i] = []
        for ti in times:
            d[ti[0]].append([ti[1], ti[2]])

        dis = [100000000] * (n + 1)
        dis[k] = 0

        q = [[0, k]]
        heapq.heapify(q)
        while len(q) != 0:
            t = heapq.heappop(q)
            if t[0] > dis[t[1]]:
                continue

            for tar, di in d[t[1]]:
                if dis[tar] > dis[t[1]] + di:
                    dis[tar] = dis[t[1]] + di
                    heapq.heappush(q, [dis[tar], tar])

        mm = 0
        for i in range(1, len(dis)):
            mm = max(mm, dis[i])

        return mm if mm != 100000000 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

