# 793. 阶乘函数后 K 个零
# https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/


from functools import lru_cache
from typing import Callable, Sequence, Tuple


# 逻辑正确，但是超时，划去
# class Solution:
#     def preimageSizeFZF(self, k: int) -> int:

#         d = dict()

#         def get_2_5(n: int) -> Tuple[int, int]:

#             if n == 0:
#                 return 0, 0

#             if n in d:
#                 return d[n]

#             if n % 2 == 0:
#                 n2, n5 = get_2_5(n // 2)
#                 d[n] = n2 + 1, n5
#                 return d[n]

#             if n % 5 == 0:
#                 n2, n5 = get_2_5(n // 5)
#                 d[n] = n2, n5 + 1
#                 return d[n]

#             d[n] = 0,0
#             return d[n]

#         ans = 0
#         n2 = 0
#         n5 = 0
#         i = 0
#         while True:
#             n2_, n5_ = get_2_5(i)
#             print(i,n2_,n5_)
#             n2 += n2_
#             n5 += n5_
#             if min(n2, n5) == k:
#                 ans += 1
#             elif min(n2, n5) > k:
#                 break

#             i += 1

#         return ans


import bisect


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        @lru_cache()
        def getz(n: int) -> int:
            ans = 0
            while n != 0:
                n = n // 5
                ans += n
            return ans

        def my_bisect_left(nums: Sequence[int], k: int) -> int:
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2
                t = getz(nums[m])
                if t > k:
                    r = m - 1
                elif t == k:
                    r = m - 1
                elif t < k:
                    l = m + 1

            if l >= len(nums):
                return len(nums)

            return l

        def mk(k: int) -> int:
            return my_bisect_left(range(5 * k), k)

        return mk(k + 1) - mk(k)


if __name__ == "__main__":
    so = Solution()
    print(so.preimageSizeFZF(0))
