# 面试题 01.04. 回文排列
# https://leetcode-cn.com/problems/palindrome-permutation-lcci/

################################################################################
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cou = Counter(s)

        isEven = len(s) % 2 == 0

        if isEven:
            for k, v in cou.items():
                if v % 2 == 1:
                    return False
        else:
            getOdd = False
            for k, v in cou.items():
                if v % 2 == 1:
                    if getOdd:
                        return False
                    getOdd = True
        return True

#################################################################################
