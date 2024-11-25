import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nexts = dict()
        for i in range(n + 1):
            nexts[i] = []
        for x,y,z in times:
            nexts[x].append((y, z))

        pq = [[0, k]]
        heapq.heapify(pq)

        MAX_INF: int = 99999999999
        dist = [MAX_INF] * (n + 1)
        dist[k] = 0

        while len(pq) > 0:
            d, t = heapq.heappop(pq)

            for y, z in nexts[t]:
                if d + z < dist[y]:
                    dist[y] = d + z
                    pq.append([dist[y], y])

        ans = 0
        for i in range(1, n + 1):
            if dist[i] == MAX_INF:
                return -1
            ans = max(ans, dist[i])
        return ans

so = Solution()
print(so.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))