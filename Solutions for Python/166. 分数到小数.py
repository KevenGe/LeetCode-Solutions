# 166. 分数到小数
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/

################################################################################


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        isNegative = False
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            isNegative = True
            numerator = -numerator if numerator < 0 else numerator
            denominator = -denominator if denominator < 0 else denominator

        intergerNum, left = divmod(numerator, denominator)

        if left == 0:
            if intergerNum == 0:
                return str(intergerNum)
            else:
                if isNegative:
                    return str(-intergerNum)
                else:
                    return str(intergerNum)

        a = left
        b = denominator
        d = dict()
        decimals = []
        targetIndex = -1
        for i in range(10005):
            if a == 0:
                break
            a = a * 10
            if a in d:
                targetIndex = d[a]
                break
            else:
                d[a] = i
                c, e = divmod(a, b)
                decimals.append(str(c))
                a = e

        if targetIndex != -1:
            decimals.insert(targetIndex, "(")
            decimals.append(")")

        if isNegative:
            return "-" + str(intergerNum) + "." + "".join(decimals)
        else:
            return str(intergerNum) + "." + "".join(decimals)


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.fractionToDecimal(27, 12))
