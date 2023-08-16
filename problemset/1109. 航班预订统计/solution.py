# 1109. 航班预订统计
# https://leetcode-cn.com/problems/corporate-flight-bookings/

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cha = [0] * (n + 2)

        for fir, las, ses in bookings:
            cha[fir] += ses
            cha[las + 1] -= ses

        ans = [0] * n
        ans[0] = cha[1]
        for i in range(1, n):
            ans[i] = ans[i - 1] + cha[i + 1]
        return ans


if __name__ == "__main__":
    solution = Solution()
