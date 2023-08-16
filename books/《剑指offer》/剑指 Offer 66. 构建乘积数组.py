# 剑指 Offer 66. 构建乘积数组
# https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b = [1] * len(a)

        t = 1
        for i in range(len(a)):
            b[i] = t
            t = t * a[i]

        t = 1
        for i in reversed(list(range(len(a)))):
            b[i] *= t
            t = t * a[i]

        return b


if __name__ == "__main__":
    solution = Solution()
