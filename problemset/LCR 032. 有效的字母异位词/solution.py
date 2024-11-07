from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if s == t:
            return False

        sc = Counter(s)
        tc = Counter(t)

        if len(sc) != len(tc):
            return False

        for k in sc.keys():
            if sc[k] != tc[k]:
                return False

        return True
