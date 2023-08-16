# 343. 整数拆分
# https://leetcode-cn.com/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:
        a, b = divmod(n, 3)
        if b == 0:
            if a == 1:
                return 2
            else:
                b = 1
        elif b == 1:
            a -= 1
            b = 2 * 2
        elif b == 2:
            if a == 0:
                return 1
        return (3 ** a) * b
