# 598. 范围求和 II
# https://leetcode-cn.com/problems/range-addition-ii/

################################################################################
from typing import List
from functools import reduce


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n

        return reduce(lambda x, y: x * y, map(lambda x: min(x), zip(*ops)), 1)


################################################################################

if __name__ == "__main__":
    solution = Solution()
