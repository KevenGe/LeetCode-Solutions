# 剑指 Offer 31. 栈的压入、弹出序列
# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        sta = []
        i = 0
        for p in popped:
            if len(sta) != 0:
                if sta[-1] == p:
                    sta.pop()
                    continue

            for j in range(i, len(pushed)):
                if pushed[j] != p:
                    sta.append(pushed[j])
                    i += 1
                else:
                    break

            if i == len(pushed):
                return False
            else:
                i += 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.validateStackSequences([2,1,0],[2,1,0]))

