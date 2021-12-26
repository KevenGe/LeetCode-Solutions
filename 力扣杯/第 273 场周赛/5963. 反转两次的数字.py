# 5963. 反转两次的数字
# https://leetcode-cn.com/contest/weekly-contest-273/problems/a-number-after-a-double-reversal/


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True
