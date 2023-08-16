# 1475. 商品折扣后的最终价格
# https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/

# from typing import List


# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         ans = []
#         for price_idx in range(len(prices)):

#             discount = 0
#             for discount_idx in range(price_idx + 1, len(prices)):
#                 if prices[discount_idx] <= prices[price_idx]:
#                     discount = prices[discount_idx]
#                     break

#             ans.append(prices[price_idx] - discount)

#         return ans


from typing import List

# 单调栈
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        st = []
        for price in reversed(prices):
            if len(st) == 0:
                st.append(price)
                ans.append(price)
            else:
                while len(st) != 0 and st[-1] > price:
                    st.pop()

                if len(st) == 0:
                    ans.append(price)
                else:
                    ans.append(price - st[-1])

                st.append(price)

        ans = list(reversed(ans))
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.finalPrices([8, 7, 4, 2, 8, 1, 7, 7, 10, 1]))
