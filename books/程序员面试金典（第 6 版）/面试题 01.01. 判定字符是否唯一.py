# 面试题 01.01. 判定字符是否唯一
# https://leetcode-cn.com/problems/is-unique-lcci/


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))


if __name__ == "__main__":
    solution = Solution()
