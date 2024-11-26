from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        return len(list(filter(
            lambda i: colors[i] ^ colors[(i + 1) % len(colors)] == 1 and colors[(i + 1) % len(colors)] ^ colors[
                (i + 2) % len(colors)] == 1, range(len(colors)))))
