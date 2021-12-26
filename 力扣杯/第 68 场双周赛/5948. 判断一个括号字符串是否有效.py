# 5948. 判断一个括号字符串是否有效
# https://leetcode-cn.com/contest/biweekly-contest-68/problems/check-if-a-parentheses-string-can-be-valid/


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        high = 0
        low = 0
        for i, lock in enumerate(locked):
            if lock == "1":
                if s[i] == "(":
                    high += 1
                    low += 1
                else:
                    high -= 1
                    if high < 0:
                        return False
                    low -= 1
                    if low < 0:
                        low = 0
            else:
                high += 1
                low -= 1
                if low < 0:
                    low = 0

        if low <= 0 and high >= 0 and high % 2 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.canBeValid("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
                              "100011110110011011010111100111011101111110000101001101001111"))
