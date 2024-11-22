from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:

        next = [i + 1 for i in range(n + 1)]

        ans = []
        cur_dist = n - 1
        for x, y in queries:
            if next[x] == -1 or y <= next[x]:
                ans.append(cur_dist)
                continue

            next[x], z = y, next[x]
            while z < y:
                cur_dist -= 1
                next[z], z = -1, next[z]

            ans.append(cur_dist)
        return ans
