from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = dict()
        for s in strs:
            s2 = "".join(sorted(s))
            if s2 not in d:
                d[s2] = []
            d[s2].append(s)

        return list(d.values())
