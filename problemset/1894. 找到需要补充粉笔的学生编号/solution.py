# 1894. 找到需要补充粉笔的学生编号
# https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk/

################################################################################

from typing import List
65
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        k = k % sums

        for i in range(len(chalk)):
            k = k - chalk[i]
            if k < 0:
                return i


################################################################################

if __name__ == "__main__":
    solution = Solution()
