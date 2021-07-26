# 1713. 得到子序列的最少操作次数
# https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence/

from typing import List
import bisect


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {}
        for i, t in enumerate(target):
            d[t] = i

        n = []
        for a in arr:
            if a in d:
                n.append(d[a])

        ans = len(target) - self.best(n)
        return ans

    def best(self, nums: List[int]) -> int:
        t = 10 ** 10
        dp = [t] * (len(nums) + 1)
        for num in nums:
            n = bisect.bisect_left(dp, num)
            dp[n] = num
        for i in range(len(dp)):
            if dp[i] == t:
                return i

    def bs(self, nums: List[int], tar: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < tar:
                l = m + 1
            else:
                r = m - 1
        return l


if __name__ == "__main__":
    solution = Solution()
