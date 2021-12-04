# 383. 赎金信
# https://leetcode-cn.com/problems/ransom-note/

################################################################################
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cou1 = Counter(ransomNote)
        cou2 = Counter(magazine)

        for k, v in cou1.items():
            if not (k in cou2 and cou2[k] >= v):
                return False
        return True

################################################################################
