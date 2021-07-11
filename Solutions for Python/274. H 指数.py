from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i = 0
        counters = [0] * (n + 1)
        while i < n:
            if citations[i] >= n:
                counters[n] += 1
            else:
                counters[citations[i]] += 1
            i += 1

        t = 0
        for i in range(len(counters)-1, -1, -1):
            t += counters[i]
            if t >= i:
                return i
        return 0

if __name__ == "__main__":
    so = Solution()
    print([1,3,1])
    print(so.hIndex([1,3,1]))