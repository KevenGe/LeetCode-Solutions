# 剑指 Offer 65. 不用加减乘除做加法
# https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/


class Solution:
    def add(self, a: int, b: int) -> int:
        t = 0xFFFFFFFF
        a = a & t
        b = b & t

        while b != 0:
            b, a = ((a & b) << 1) & t, (a ^ b)
        return a if a <= 0x7FFFFFFF else ~(a ^ t)


if __name__ == "__main__":
    solution = Solution()
    print(solution.add(121, 212))
