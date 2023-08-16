# 剑指 Offer 58 - I. 翻转单词顺序
# https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/


class Solution:
    def reverseWords(self, s: str) -> str:
        s2 = list(filter(lambda x: x != "", s.split(" ")))
        s3 = list(reversed(s2))
        return " ".join(s3).strip()


if __name__ == "__main__":
    solution = Solution()
