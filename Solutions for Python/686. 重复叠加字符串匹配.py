# 686. 重复叠加字符串匹配
# https://leetcode-cn.com/problems/repeated-string-match/

import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(b) == 0:
            return 0
        next = self.init_next(b)

        i = 0
        j = 0
        c_n = math.ceil((len(b) - 1 + len(a)) / len(a))
        while i < c_n * len(a) and j < len(b):
            if a[i % len(a)] == b[j]:
                i += 1
                j += 1
            else:
                j = next[j]
                if j == -1:
                    j = 0
                    i += 1
                if i - j > len(a) - 1:
                    break

        if j == len(b):
            return (i - 1) // len(a) + 1
        else:
            return -1

    def init_next(self, b: str):
        next = [0] * len(b)
        next[0] = -1

        for i in range(2, len(b)):
            k = next[i - 1]
            while k != -1:
                if b[i - 1] == b[k]:
                    next[i] = k + 1
                    break
                else:
                    k = next[k]
        return next


if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatedStringMatch("aaac", "aac"))
