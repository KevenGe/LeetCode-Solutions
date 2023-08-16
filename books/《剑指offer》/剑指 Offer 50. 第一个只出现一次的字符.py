# 剑指 Offer 50. 第一个只出现一次的字符
# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((s[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return " " if not q else q[0][0]


if __name__ == "__main__":
    solution = Solution()
