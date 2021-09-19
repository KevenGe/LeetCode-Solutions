# 650. 只有两个键的键盘
# https://leetcode-cn.com/problems/2-keys-keyboard/

################################################################################

import math


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [100000000] * 1001  # 到当前位置的次数
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, math.floor(math.sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
                    dp[i] = min(dp[i], dp[i // j] + j)

        return dp[n]


################################################################################

if __name__ == "__main__":
    solution = Solution()
