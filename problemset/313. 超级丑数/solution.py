# 313. 超级丑数
# https://leetcode-cn.com/problems/super-ugly-number/

from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        choushu = [1]
        pp = [0] * len(primes)

        for i in range(1, n):

            m = float("inf")
            waitToAdd = []
            for i in range(len(primes)):
                t = primes[i] * choushu[pp[i]]
                if m > t:
                    m = t
                    waitToAdd = [i]
                elif m == t:
                    waitToAdd.append(i)

            choushu.append(m)
            for w in waitToAdd:
                pp[w] += 1

        return choushu[n - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.nthSuperUglyNumber(1, [2, 3, 5]))

