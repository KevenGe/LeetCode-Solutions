from typing import List
from functools import reduce


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        total = reduce(lambda x, y: x ^ y, range(1, len(encoded) + 2))
        newTotal = reduce(
            lambda x, y: x ^ y, [encoded[i] for i in range(1, len(encoded), 2)]
        )

        ans = [0 for i in range(len(encoded) + 1)]
        ans[0] = total ^ newTotal

        for i in range(1, len(encoded) + 1):
            ans[i] = encoded[i - 1] ^ ans[i - 1]
        return ans
