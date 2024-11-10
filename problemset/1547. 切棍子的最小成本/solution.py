from typing import List

# Old Version
# class Solution:
#     def minCost(self, n: int, cuts: List[int]) -> int:
#         cuts_num = len(cuts)
#         cuts = [0] + sorted(cuts) + [n]
#         dp = [[0 for _ in range(cuts_num + 1)] for _ in range(cuts_num + 1)]

#         for i in range(cuts_num + 1):
#             for j in range(cuts_num + 1):
#                 if i == 0:
#                     continue
#                 if j + i > cuts_num:
#                     continue
#                 dp[j][j + i] = min(
#                     [dp[j][z] + dp[z + 1][j + i] for z in range(j, j + i)]
#                 )
#                 dp[j][j + i] += cuts[j + i + 1] - cuts[j]

#         return dp[0][cuts_num]


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts_num = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        dp = [[0 for _ in range(cuts_num + 1)] for _ in range(cuts_num + 1)]

        for i in range(1, cuts_num + 1):
            for j in range(cuts_num - i, -1, -1):
                if j + i > cuts_num:
                    continue
                dp[j][j + i] = min(
                    [dp[j][z] + dp[z + 1][j + i] for z in range(j, j + i)]
                )
                dp[j][j + i] += cuts[j + i + 1] - cuts[j]

        return dp[0][cuts_num]


so = Solution()
print(so.minCost(7, [1, 3, 4, 5]))
