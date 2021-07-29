# 1104. 二叉树寻路
# https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/

from typing import List
import math


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        while label != 1:
            ans.insert(0, label)
            par = label // 2
            recordPar = self.getReversedPar(par)
            label = recordPar
        ans.insert(0, 1)
        return ans

    def getReversedPar(self, par: int) -> int:
        s = math.floor(math.log2(par))
        start = 2 ** s
        end = 2 ** (s + 1) - 1
        res = (end - par) + start
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.pathInZigZagTree(14))
