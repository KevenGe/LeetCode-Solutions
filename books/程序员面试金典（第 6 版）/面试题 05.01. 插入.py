# 面试题 05.01. 插入
# https://leetcode-cn.com/problems/insert-into-bits-lcci/


class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:

        t = 1
        for ji in range(j - i):
            t = (t << 1) + 1

        for ii in range(i):
            t = t << 1

        n = (N | t) ^ t

        for ii in range(i):
            M = M << 1

        n = n | M
        return n


if __name__ == '__main__':
    solution = Solution()
    print(solution.insertBits(1024, 19, 2, 6))
