# 646. 最长数对链
# https://leetcode.cn/problems/maximum-length-of-pair-chain/


from typing import List

# 动态规划
# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort(key=lambda x: x[0])
#         dp = [1] * len(pairs)

#         for i in range(len(pairs)):
#             for j in range(i):
#                 if pairs[i][0] > pairs[j][1]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

# 贪心，最快算法
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        last_b = -float("inf")
        ans = 0
        for i in range(len(pairs)):
            if pairs[i][0] > last_b:
                last_b = pairs[i][1]
                ans += 1
        return ans


if __name__ == "__main__":
    so = Solution()
    # print(so.findLongestChain())
