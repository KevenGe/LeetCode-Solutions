# 541. 反转字符串 II
# https://leetcode-cn.com/problems/reverse-string-ii/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            l = i
            r = i + k - 1
            if r >= len(s):
                r = len(s) - 1

            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        s = "".join(s)
        return s


if __name__ == "__main__":
    solution = Solution()
