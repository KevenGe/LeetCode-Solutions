# 面试题 01.05. 一次编辑
# https://leetcode-cn.com/problems/one-away-lcci/

################################################################################


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first) - len(second)) >= 2:
            return False
        elif len(first) == len(second):
            badOccured = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    if badOccured:
                        return False
                    badOccured = 1
            return True
        else:
            if len(first) > len(second):
                first, second = second, first

            badOccured = 0
            for i in range(len(first)):
                if first[i] != second[i + badOccured]:
                    if badOccured or first[i] != second[i + 1]:
                        return False
                    else:
                        badOccured = 1
            return True


################################################################################
