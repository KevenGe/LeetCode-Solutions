from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_map = dict([(c, i) for i, c in enumerate(order)])

        def my_cmp(a: str, b: str):
            # a < b

            an = len(a)
            bn = len(b)
            n = max(an, bn)

            for i in range(n):
                if i >= an and i < bn:
                    break

                if i <= an and i >= bn:
                    return False

                if a[i] == b[i]:
                    continue

                ao = order_map[a[i]]
                bo = order_map[b[i]]

                if ao < bo:
                    break

                return False

            return True

        for i in range(len(words) - 1):
            if my_cmp(words[i], words[i + 1]) == False:
                return False

        return True
