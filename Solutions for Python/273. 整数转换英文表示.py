# 273. 整数转换英文表示
# https://leetcode-cn.com/problems/integer-to-english-words/

################################################################################


class Solution:
    def numberToWords(self, num: int) -> str:
        def to1(s: int) -> str:
            if s == 0:
                return "Zero"
            elif s == 1:
                return "One"
            elif s == 2:
                return "Two"
            elif s == 3:
                return "Three"
            elif s == 4:
                return "Four"
            elif s == 5:
                return "Five"
            elif s == 6:
                return "Six"
            elif s == 7:
                return "Seven"
            elif s == 8:
                return "Eight"
            elif s == 9:
                return "Nine"
            elif s == 10:
                return "Ten"
            elif s == 11:
                return "Eleven"
            elif s == 12:
                return "Twelve"
            elif s == 13:
                return "Thirteen"
            elif s == 14:
                return "Fourteen"
            elif s == 15:
                return "Fifteen"
            elif s == 16:
                return "Sixteen"
            elif s == 17:
                return "Seventeen"
            elif s == 18:
                return "Eighteen"
            elif s == 19:
                return "Nineteen"

        def to2(s: int) -> str:
            if s < 20:
                return to1(s)
            else:
                ans = []
                n = s // 10
                if n == 2:
                    ans.append("Twenty")
                elif n == 3:
                    ans.append("Thirty")
                elif n == 4:
                    ans.append("Forty")
                elif n == 5:
                    ans.append("Fifty")
                elif n == 6:
                    ans.append("Sixty")
                elif n == 7:
                    ans.append("Seventy")
                elif n == 8:
                    ans.append("Eighty")
                elif n == 9:
                    ans.append("Ninety")

                t = s % 10
                if t != 0:
                    ans.append(to1(t))
                return " ".join(ans)

        def to3(s: int) -> str:

            ans = []

            if s >= 100:
                n = s // 100
                s = s % 100
                ans.append(to1(n))
                ans.append("Hundred")

            if s != 0:
                ans.append(to2(s))
            return " ".join(ans)

        def to4(s: int) -> str:
            if s == 0:
                return "Zero"

            ans = []

            tlist = ["Thousand", "Million", "Billion"]

            for i in range(6):
                t = s % 1000
                s = s // 1000

                if t != 0:
                    if i >= 1:
                        ans.append(tlist[i - 1])
                    ans.append(to3(t))
                if s == 0:
                    break

            return " ".join(reversed(ans))

        return to4(num)


################################################################################

if __name__ == "__main__":
    s = Solution()
    print(s.numberToWords(1000))
