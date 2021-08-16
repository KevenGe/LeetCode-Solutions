# 剑指 Offer 59 - I. 滑动窗口的最大值
# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        dp = []
        for i in range(k):
            dp.append((-nums[i], i))
        heapq.heapify(dp)
        # print(dp)

        ans = [-dp[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(dp, (-nums[i], i))
            while dp[0][1] <= i - k:
                heapq.heappop(dp)
            ans.append(-dp[0][0])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

