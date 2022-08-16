# 1656. 设计有序流
# https://leetcode.cn/problems/design-an-ordered-stream/

from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.l = [""] * (n + 1)
        self.p = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        if self.p == idKey:
            ans = []
            self.l[idKey] = value
            for p in range(self.p, self.n + 1):
                if self.l[p] != "":
                    ans.append(self.l[p])
                else:
                    self.p = p
                    break

            return ans
        else:
            self.l[idKey] = value
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
