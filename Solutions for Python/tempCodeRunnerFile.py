from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = 0
        counters = [0] * (n + 1)
        while i < n:
            if citations[i] >= n: