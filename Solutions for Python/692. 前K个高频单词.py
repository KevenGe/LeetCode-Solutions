from typing import List
from functools import cmp_to_key


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maps = dict()
        for word in words:
            if word in maps:
                maps[word] += 1
            else:
                maps[word] = 1

        l = []
        for key, value in maps.items():
            l.append((key, value))

        def cmp(a, b):
            t = b[1] - a[1]
            if t != 0:
                return t
            else:
                return 1 if b[0] > a[0] else 0

        l.sort(key=cmp_to_key(lambda x, y: y[1] - x[1]))

        ans = []
        for i in range(k):
            ans.append(l[i][0])

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
