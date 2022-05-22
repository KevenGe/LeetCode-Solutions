# 464. 我能赢吗
# https://leetcode.cn/problems/can-i-win/


from typing import List
from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal > sum(list(range(1, maxChoosableInteger + 1))):
            return False

        if desiredTotal == 0:
            return True

        @lru_cache(99999999999)
        def dfs(chooseNum:int, lastTotal:int) -> bool:
            if lastTotal <= 0:
                return False
            else:
                IWillWin = False
                for i in range(maxChoosableInteger):
                    if not ((1 << i) & chooseNum):
                        newChooseNum = (1 << i) | chooseNum
                        r = dfs(newChooseNum, lastTotal - (i + 1))
                        if r == False:
                            IWillWin = True
                            break
                return IWillWin

        return dfs(0, desiredTotal)


if __name__ == "__main__":
    so = Solution()
    print(so.canIWin(10, 0))
    print(so.canIWin(10, 1))
    print(so.canIWin(10, 11))
    print(so.canIWin(18, 79))
    print(so.canIWin(20, 152))
