from itertools import product
from math import floor
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        
        ans = [[0 for _ in range(n)]for _ in range(m)]
        for i,j in product(range(m), range(n)):
            ts = []
            for di, dj in product([-1, 0, 1], [-1, 0, 1]):
                ni = i + di
                nj = j + dj

                if not(0 <= ni < m and 0 <= nj < n):
                    continue
                ts.append(img[ni][nj])
            ans[i][j] = floor(sum(ts) / len(ts))
        return ans