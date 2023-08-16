# 面试题 01.09. 字符串轮转
# https://leetcode-cn.com/problems/string-rotation-lcci/


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return ((s1 + s1).find(s2) != -1) if len(s1) == len(s2) else False

