# 871. 最低加油次数
# https://leetcode.cn/problems/minimum-number-of-refueling-stops/


from typing import List
from queue import PriorityQueue


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel

        for i in range(1, len(dp)):
            for j in range(i - 1, -1, -1):
                if dp[j] >= stations[i - 1][0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i - 1][1])

        ans = -1
        for i in range(len(dp)):
            if dp[i] >= target:
                ans = i
                break

        return ans


from queue import PriorityQueue


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pri = PriorityQueue()

        cur_dist = startFuel

        count = 0

        for i in range(len(stations)):
            if cur_dist >= stations[i][0]:
                pri.put_nowait(-stations[i][1])
            else:

                while True:
                    if pri.qsize() == 0:
                        return -1

                    cur_dist = cur_dist + (-pri.get_nowait())
                    count += 1

                    if cur_dist >= stations[i][0]:
                        break

                pri.put_nowait(-stations[i][1])

        if cur_dist >= target:
            return count
        else:

            while True:
                if pri.qsize() == 0:
                    return -1

                cur_dist = cur_dist + (-pri.get_nowait())
                count += 1

                if cur_dist >= target:
                    break

            return count


if __name__ == "__main__":
    so = Solution()
    assert so.minRefuelStops(100, 25, [[25, 25], [50, 25], [75, 25]]) == 3
