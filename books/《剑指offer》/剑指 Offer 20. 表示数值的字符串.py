# 剑指 Offer 20. 表示数值的字符串


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if s.find("e") != -1 or s.find("E") != -1:
            t1 = s.find("e")
            t2 = s.find("E")
            t = t1 if t1 != -1 else t2

            s_before = s[0:t]
            s_after = s[t + 1 :]

            return (
                self.isLittleNumber(s_before) or self.isZhengNumber(s_before)
            ) and self.isZhengNumber(s_after)
        else:
            return self.isLittleNumber(s) or self.isZhengNumber(s)

    def isLittleNumber(self, s: str) -> bool:
        """判断小数"""
        if len(s) == 0:
            return False

        if s[0] == "+" or s[0] == "-":
            if len(s) == 1:
                return False
            s = s[1:]

        t = s.find(".")
        if t == -1:
            return False

        sBefLen = t
        sAftLen = len(s) - t - 1

        if sBefLen == 0:
            if sAftLen == 0:
                return False
            else:
                return self.isZhengNumber(s[t + 1 :], noSign=True)
        else:
            if sAftLen == 0:
                return self.isZhengNumber(s[0:t])
            else:
                return self.isZhengNumber(s[0:t]) and self.isZhengNumber(
                    s[t + 1 :], noSign=True
                )

    def isZhengNumber(self, s: str, noSign=False) -> bool:
        """判断整数"""
        if len(s) == 0:
            return False

        if s[0] == "+" or s[0] == "-":
            if noSign or len(s) == 1:
                return False
            s = s[1:]

        isOK = False
        for c in s:
            if c.isdigit():
                isOK = True
            else:
                isOK = False
                break
        return isOK


if __name__ == "__main__":
    so = Solution()
    print(so.isNumber("4E-2"))
    print(so.isNumber("3.-4"))

