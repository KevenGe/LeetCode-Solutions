
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = dict(items1)
        for k,v in items2:
            if k in d:
                d[k] += v
            else:
                d[k] = v

        return list(sorted(list(d.items()), key=lambda x:x[0]))


if __name__ == "__main__":
    so = Solution()
    print(so.mergeSimilarItems([[1,1],[4,5],[3,8]],[[3,1],[1,5]]))
    # assert so.mergeSimilarItems([[1,1],[4,5],[3,8]],[[3,1],[1,5]]) == [[1,6],[3,9],[4,5]]
    print(so.mergeSimilarItems([[1,1],[3,2],[2,3]], [[2,1],[3,2],[1,3]]))