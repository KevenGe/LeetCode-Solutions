# 787. K 站中转内最便宜的航班
# https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dp = [float("inf")] * n
        for flight in flights:
            if flight[0] == src:
                dp[flight[1]] = flight[2]
        dp[src] = 0

        ans = dp[dst]
        for i in range(0, k):
            newDp = dp.copy()
            for flight in flights:
                if flight[0] == float("inf"):
                    continue

                t = dp[flight[0]] + flight[2]
                if t < newDp[flight[1]]:
                    newDp[flight[1]] = t

            dp = newDp
            ans = min(ans, dp[dst])
        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findCheapestPrice(
            5,
            [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
            2,
            1,
            1,
        )
    )

