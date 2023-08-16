# 638. 大礼包
# https://leetcode-cn.com/problems/shopping-offers/

################################################################################
# from typing import List
# import copy


# class Solution:
#     def shoppingOffers(
#         self, price: List[int], special: List[List[int]], needs: List[int]
#     ) -> int:
#         def runs(index: int, dp):
#             if index < len(needs):
#                 t = runs(index + 1, dp)
#                 t2 = [copy.copy(t) for j in range(needs[index])]
#                 return t2
#             else:
#                 return 0

#         dp = runs(999999999, [])
#         print(dp)

#         def runs(index: int, index2: List[int], dp):
#             if index < len(needs) - 1:
#                 for i in range(needs[index]):
#                     index2[index] = i
#                     runs(index + 1, index2, dp)
#             else:

#                 for j in range(needs[index]):
#                     if j == 0:
#                         pass
#                 def runs2(index3: int):
#                     pass

################################################################################


# from functools import lru_cache

# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#         n = len(price)

#         # 过滤不需要计算的大礼包，只保留需要计算的大礼包
#         filter_special = []
#         for sp in special:
#             if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
#                 filter_special.append(sp)

#         # 记忆化搜索计算满足购物清单所需花费的最低价格
#         @lru_cache(None)
#         def dfs(cur_needs):
#             # 不购买任何大礼包，原价购买购物清单中的所有物品
#             min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
#             for cur_special in filter_special:
#                 special_price = cur_special[-1]
#                 nxt_needs = []
#                 for i in range(n):
#                     if cur_special[i] > cur_needs[i]:  # 不能购买超出购物清单指定数量的物品
#                         break
#                     nxt_needs.append(cur_needs[i] - cur_special[i])
#                 if len(nxt_needs) == n:  # 大礼包可以购买
#                     min_price = min(min_price, dfs(tuple(nxt_needs)) + special_price)
#             return min_price

#         return dfs(tuple(needs))

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/shopping-offers/solution/da-li-bao-by-leetcode-solution-p1ww/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
################################################################################
from typing import List
from functools import lru_cache


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:

        # 过滤
        newSpecial = []
        for spe in special:
            t = 0
            for i in range(len(price)):
                t += spe[i] * price[i]
            if t > spe[-1]:
                newSpecial.append(spe)
        special = newSpecial

        @lru_cache(maxsize=None)
        def dfs(needs):
            pri = 0
            for i in range(len(needs)):
                pri += needs[i] * price[i]

            for spe in special:
                newNeeds = []
                for i in range(len(needs)):
                    if spe[i] <= needs[i]:
                        newNeeds.append(needs[i] - spe[i])
                    else:
                        break

                if len(newNeeds) == len(needs):
                    pri = min(pri, spe[-1] + dfs(tuple(newNeeds)))

            return pri

        return dfs(tuple(needs))


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]))

