# 438. 找到字符串中所有字母异位词
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pl = [0] * 26
        for pt in p:
            pl[ord(pt) - ord("a")] += 1

        ans = []

        sl = pl.copy()
        for i in range(len(p)):
            sl[ord(s[i]) - ord("a")] -= 1

        isOK = True
        for i in range(26):
            if sl[i] != 0:
                isOK = False
                break
        if isOK:
            ans.append(0)

        for i in range(len(p), len(s)):
            sl[ord(s[i]) - ord("a")] -= 1
            sl[ord(s[i - len(p)]) - ord("a")] += 1

            isOK = True
            for j in range(26):
                if sl[j] != 0:
                    isOK = False
                    break
            if isOK:
                ans.append(i - len(p) + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
