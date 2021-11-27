# 519. 随机翻转矩阵
# https://leetcode-cn.com/problems/random-flip-matrix/

################################################################################
import random
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.r = m * n
        self.map = {}

    def flip(self) -> List[int]:
        t = random.randint(0, self.r - 1)
        tc = t
        while tc in self.map:
            tc = self.map[tc]

        i = tc // self.n
        j = tc % self.n

        self.map[t] = self.r - 1
        self.r -= 1

        return [i, j]

    def reset(self) -> None:
        self.r = self.m * self.n
        self.map.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

################################################################################


if __name__ == '__main__':
    solution = Solution(10, 10)
    for i in range(100):
        print(solution.flip())
