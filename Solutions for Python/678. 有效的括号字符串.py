# 678. 有效的括号字符串
# https://leetcode-cn.com/problems/valid-parenthesis-string/

################################################################################


class Solution:
    def checkValidString(self, s: str) -> bool:
        smin = 0
        smax = 0
        for i in range(len(s)):
            if s[i] == "(":
                smin += 1
                smax += 1
            elif s[i] == ")":
                smin = max(smin - 1, 0)
                smax -= 1
                if smax < 0:
                    return False

            else:
                smin = max(smin - 1, 0)
                smax += 1

        return smin == 0


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

