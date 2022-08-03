# 剑指 Offer II 002. 二进制加法
# https://leetcode.cn/problems/JFETK5/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    so = Solution()
    print(so.addBinary("11", "10") == "101")
    print(so.addBinary("1010", "1011") == "10101")
