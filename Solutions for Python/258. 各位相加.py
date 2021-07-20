# 258. 各位相加
# https://leetcode-cn.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            for n in list(str(num)):
                s += int(n)
            num = s
        return num


if __name__ == "__main__":
    so = Solution()
    print(so.addDigits(38))
