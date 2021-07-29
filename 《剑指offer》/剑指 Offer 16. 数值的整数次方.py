# 剑指 Offer 16. 数值的整数次方
# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        t = x
        while n != 0:
            if n & 1:
                ans = ans * t
            n = n >> 1
            if n != 0:
                t = t ** 2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2.00000, -2147483648))

