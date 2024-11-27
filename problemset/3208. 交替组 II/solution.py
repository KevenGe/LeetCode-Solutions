from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        cur_len = 1
        for i in range(1, k):
            if colors[i] ^ colors[i - 1]:
                cur_len += 1
            else:
                cur_len = 1

        ans: int = 0
        for i in range(k, k + n):
            a = i % n
            b = (i - 1) % n
            if colors[a] ^ colors[b]:
                cur_len += 1
            else:
                cur_len = 1

            if cur_len >= k:
                ans += 1

        return ans
