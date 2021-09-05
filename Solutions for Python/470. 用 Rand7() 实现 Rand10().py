# 470. 用 Rand7() 实现 Rand10()
# https://leetcode-cn.com/problems/implement-rand10-using-rand7/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random


def rand7():
    return random.randint(1, 7)


# class Solution:
#     def rand10(self):
#         """
#         :rtype: int
#         """
#         t = (
#             rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#             + rand7()
#         ) % 10 + 1
#         return t


# ! 拒绝选择
# class Solution:
#     def rand10(self):
#         """
#         :rtype: int
#         """
#         x = (rand7() - 1) * 7 + rand7()
#         while x > 40:
#             x = (rand7() - 1) * 7 + rand7()
#         return (x - 1) % 10 + 1


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x = rand7()
        while x > 5:
            x = rand7()

        y = rand7()
        while y == 7:
            y = rand7()
        y = y % 2

        z = x + y * 5
        return z


if __name__ == "__main__":
    solution = Solution()
