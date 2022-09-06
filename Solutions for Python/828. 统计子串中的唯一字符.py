# 828. 统计子串中的唯一字符
# https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/

from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last_left = [-1] * len(s)
        last_right = [-1] * len(s)

        last_one = defaultdict(lambda: -1)
        for i, c in enumerate(s):
            last_left[i] = last_one[c]
            last_one[c] = i

        last_one = defaultdict(lambda: len(s))
        for i, c in enumerate(reversed(s)):
            last_right[len(s) - 1 - i] = last_one[c]
            last_one[c] = len(s) - 1 - i

        ans = 0
        for i, c in enumerate(s):
            l = i - last_left[i]
            r = last_right[i] - i
            ans += l * r
        return ans

