from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # filter for good special
        filtered_special: List[List[int]] = []
        for spec in special:
            spec_price = spec[n]
            spec_price_y = sum([price[i] * spec[i]  for i in range(n)])
            if spec_price_y > spec_price:
                filtered_special.append(spec)

        #
        @lru_cache
        def dfs(sub_need: Tuple[int]) -> int:
            no_special_price = sum([price[i] * sub_need[i]  for i in range(n)])
            min_price = no_special_price
            for spec in filtered_special:
                remain_need: List[int] = []
                for i in range(n):
                    if spec[i] > sub_need[i]:
                        break
                    remain_need.append(sub_need[i] - spec[i])

                if len(remain_need) != n:
                    continue

                spec_price = spec[n]
                min_price = min(min_price, dfs(tuple(remain_need)) + spec_price)
            return min_price

        return dfs(tuple(needs))
