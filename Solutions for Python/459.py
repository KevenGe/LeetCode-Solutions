"""
LeetCode 459

https://leetcode-cn.com/problems/repeated-substring-pattern/
https://leetcode-cn.com/problems/repeated-substring-pattern/
https://leetcode-cn.com/problems/repeated-substring-pattern/

"""


class Solution:
    """
    静态类
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        题目要求

        :param s:
        :return:
        """
        for i in range(1, len(s), 1):
            if len(s) % i == 0:
                t = s[0:i]
                if self.isit(s, t):
                    return True
        return False

    def isit(self, s: str, t: str) -> bool:
        """
        判断t是否是S的循环子串


        :param s: 大串
        :param t: 小串
        :return: bool
        """
        for i in range(0, len(s), len(t)):
            if s[i:i + len(t)] != t:
                return False
        return True
