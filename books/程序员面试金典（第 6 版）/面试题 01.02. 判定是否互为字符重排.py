# 面试题 01.02. 判定是否互为字符重排
# https://leetcode-cn.com/problems/check-permutation-lcci/

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    solution = Solution()
