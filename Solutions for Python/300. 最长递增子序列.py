# 300. 最长递增子序列
# https://leetcode-cn.com/problems/longest-increasing-subsequence/

from typing import List


def bs(dp: List[int], num: int):
    l = 0
    r = len(dp) - 1
    while l <= r:
        m = (l + r) // 2
        if dp[m] < num:
            l = m + 1
        else:
            r = m - 1
    return l


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [20000] * (len(nums) + 1)
        for num in nums:
            t = bs(dp, num)
            dp[t] = num

        ans = 0
        for i in range(len(dp)):
            if dp[i] == 20000:
                ans = i
                break
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(bs([0, 1, 1, 2, 3, 3, 3, 4, 5], 0.5))
