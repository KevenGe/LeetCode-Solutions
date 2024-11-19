from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:

        pres: List[List[int]] = [[]] * n
        for i in range(n - 1):
            pres[i + 1] = [i]

        dp :List[int]= [0] * n

        for i in range(n):
            dp[i] = i

        ans = []
        for x, y in queries:
            pres[y].append(x)

            for z in range(y, n):
                for k in pres[z]:
                    dp[z] = min(dp[z], dp[k] + 1)
            ans.append(dp[-1])

        return ans
