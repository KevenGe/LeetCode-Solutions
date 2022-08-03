# 899. 有序队列
# https://leetcode.cn/problems/orderly-queue/

import copy


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        def orderk1(s: str) -> str:
            ans = copy.copy(s)
            s = list(s)
            for i in range(len(s)):
                t = "".join(s)
                s = s[1:] + s[0:1]
                if t < ans:
                    ans = t
            return ans

        def orderk2(s: str) -> str:
            s = list(s)
            s = sorted(s)
            ans = "".join(s)
            return ans

        ans = None
        if k == 1:
            ans = orderk1(s)
        else:
            ans = orderk2(s)

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.orderlyQueue("cba", 1))
