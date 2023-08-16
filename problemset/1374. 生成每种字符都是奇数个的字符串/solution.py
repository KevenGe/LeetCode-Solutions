# 1374. 生成每种字符都是奇数个的字符串
# https://leetcode.cn/problems/generate-a-string-with-characters-that-have-odd-counts/


class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return "a"
        elif n % 2 == 0:
            return "a" * (n - 1) + "b"
        elif n % 2 == 1:
            return "a" * n

