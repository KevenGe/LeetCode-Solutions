# 367. 有效的完全平方数
# https://leetcode-cn.com/problems/valid-perfect-square/

################################################################################


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i ** 2 < num:
            i += 1

        return num == i ** 2


################################################################################

if __name__ == "__main__":
    solution = Solution()
