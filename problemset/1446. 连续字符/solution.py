# 1446. 连续字符
# https://leetcode-cn.com/problems/consecutive-characters/

################################################################################


class Solution:
    def maxPower(self, s: str) -> int:
        anscou = 1

        a = s[0]
        acou = 1
        for i in range(1, len(s)):
            if a == s[i]:
                acou += 1
                if acou > anscou:
                    anscou = acou
            else:
                a = s[i]
                acou = 1
        return anscou

################################################################################
