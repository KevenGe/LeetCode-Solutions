# 400. 第 N 位数字
# https://leetcode-cn.com/problems/nth-digit/


class Solution:
    def findNthDigit(self, n: int) -> int:

        numWidth = 0
        t = 10
        for i in range(1, 100):
            if n >= t:
                n -= t
            else:
                numWidth = i
                break
            t = 9 * (10 ** i) * (i + 1)

        return int(
            list(str((10 ** (i - 1) if i - 1 > 0 else 0) + n // numWidth))[n % numWidth]
        )
