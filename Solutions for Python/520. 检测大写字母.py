# 520. 检测大写字母
# https://leetcode-cn.com/problems/detect-capital/

################################################################################
import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.search("^(([A-Z])+|([A-Z]?[a-z]*))$", word) is not None


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.detectCapitalUse("ASSsD"))
