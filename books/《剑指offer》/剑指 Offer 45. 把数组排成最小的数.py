# 剑指 Offer 45. 把数组排成最小的数
# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

from typing import List
import functools


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a: int, b: int) -> int:
            a = str(a)
            b = str(b)
            isSwaped = False
            if len(a) > len(b):
                isSwaped = True
                a, b = b, a

            maxn = len(b)

            ans = 0

            if a + b < b + a:
                ans = -1
            else:
                ans = 1

            return -ans if isSwaped else ans

        nums.sort(key=functools.cmp_to_key(cmp))
        return "".join(map(str, nums))


if __name__ == "__main__":
    solution = Solution()
    print(solution.minNumber([121,12]))
