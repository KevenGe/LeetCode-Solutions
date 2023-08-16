# 372. 超级次方
# https://leetcode-cn.com/problems/super-pow/

from typing import List
from functools import reduce


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a = a % 1337
        return reduce(lambda n, bi: (((n ** 10) % 1337) * ((a ** bi) % 1337)) % 1337, b, 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.superPow(2, [2, 1]))
