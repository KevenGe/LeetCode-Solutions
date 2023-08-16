from typing import List


# class Solution:
#     """ 动态规划
#     """
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         dp = [[0 for i in range(2002)] for i in range(21)]
#         dp[0][0] = 1
#         for index, num in enumerate(nums, 1):
#             for i in range(-1000, 1001):
#                 if i + num <= 1000:
#                     dp[index][i] += dp[index - 1][i + num]
#                 if i - num >= -1000:
#                     dp[index][i] += dp[index - 1][i - num]

#         return dp[len(nums)][target]


class Solution:
    """ 动态规划
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        neg, d = divmod((sum(nums) - target), 2)
        if d != 0:
            return 0

        dp = [0] * 1002
        dp[0] = 1

        for num in nums:
            for i in range(1000, -1, -1):
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[neg]


if __name__ == "__main__":
    so = Solution()
    print(so.findTargetSumWays([1, 1, 1, 1, 1], 3))

