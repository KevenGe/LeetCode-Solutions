# 678. 有效的括号字符串
# https://leetcode-cn.com/problems/valid-parenthesis-string/

################################################################################


class Solution:
    def checkValidString(self, s: str) -> bool:

        bracket_high_level = 0
        bracket_low_level = 0
        for c in s:
            if c == "(":
                bracket_high_level += 1
                bracket_low_level += 1
            elif c == ")":
                bracket_high_level -= 1
                bracket_low_level -= 1
            elif c == "*":
                bracket_high_level += 1
                bracket_low_level -= 1

            if bracket_high_level < 0:
                return False

            if bracket_low_level < 0:
                bracket_low_level = 0

        if bracket_low_level != 0:
            return False

        return True



################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.checkValidString(
            # "*((*((**(((*)*****((*("
            # "*("
            # "(*)"
            "**)))"
        )
    )

