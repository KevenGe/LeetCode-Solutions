# 剑指 Offer II 001. 整数除法
# https://leetcode.cn/problems/xoh6Oh/


class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)

        if b == 1:
            return a

        if b == -1:
            if a == INT_MIN:
                return INT_MAX
            else:
                return -a

        rev = False
        if a < 0:
            rev = not rev
            a = -a
        if b < 0:
            rev = not rev
            b = -b

        nb = b
        fast_adds = [0, nb]
        for i in range(30):
            nb = nb + nb
            fast_adds.append(nb)

        na = a
        ans = 0
        for i in range(31, 0, -1):
            if na >= fast_adds[i]:
                na = na - fast_adds[i]
                ans += 2 ** (i - 1)

        return -ans if rev else ans


if __name__ == "__main__":
    so = Solution()
    print(so.divide(15, 2))
    print(so.divide(7, 2))
    print(so.divide(7, -2))
    print(so.divide(7, -3))
    print(so.divide(0, 1))
    print(so.divide(1, 1))
