# 剑指 Offer 67. 把字符串转换成整数
# https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/


# 状态机


class Solution:
    def strToInt(self, str: str) -> int:

        status = 0
        """
        0：初始状态，遇见数字或者符号，变为1
        1：在此状态下，开始计算数字，遇到非数字字符，则，转到2
        2：结束字符，此状态下，字符已经计算完毕
        """

        ans = 0
        symbol = True

        for i, s in enumerate(str):
            if status == 0:
                if s.isalpha():
                    status = 2
                    break
                elif s == "+":
                    status = 1
                elif s == "-":
                    symbol = False
                    status = 1
                elif s.isdigit():
                    ans = int(s, 10)
                    status = 1
                elif s.isspace():
                    continue
                else:
                    status = 2
            elif status == 1:
                if s.isdigit():
                    ans = ans * 10 + int(s, 10)
                else:
                    status = 2

        if symbol:
            t = (2 ** 31) - 1
            if ans > t:
                ans = t
        else:
            t = -(2 ** 31)
            ans = - ans

            if ans < t:
                ans = t

        return ans


if __name__ == "__main__":
    solution = Solution()
