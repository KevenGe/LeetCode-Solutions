# 1220. 统计元音字母序列的数目
# https://leetcode-cn.com/problems/count-vowels-permutation/


################################################################################

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        rou = {
            0: [1],
            1: [0, 2],
            2: [0, 1, 3, 4],
            3: [2, 4],
            4: [0],
        }

        dp = [1 for i in range(5)]

        for i in range(1, n):
            nextDp = [0 for i in range(5)]
            for j in range(5):
                for v in rou[j]:
                    nextDp[v] = (nextDp[v] + dp[j]) % mod
            dp = nextDp

        ans = 0
        for v in dp:
            ans = (ans + v) % mod
        return ans
