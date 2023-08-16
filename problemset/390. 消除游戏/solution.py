# 390. 消除游戏
# https://leetcode-cn.com/problems/elimination-game/

# 超时
# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         arr = [i for i in range(1, n + 1)]
#         l = 0
#         r = n - 1
#
#         l2r = True
#         while l != r:
#             if l2r:
#                 tl = l
#                 tr = l + 1
#                 while tr <= r:
#                     arr[tl] = arr[tr]
#                     tl += 1
#                     tr += 2
#                 r = tl - 1
#                 l2r = False
#             else:
#                 tr = r
#                 tl = r-1
#                 while tl >= l:
#                     arr[tr] = arr[tl]
#                     tr -= 1
#                     tl -= 2
#                 l = tr + 1
#                 l2r = True
#
#         return arr[l]


class Solution:
    def lastRemaining(self, n: int) -> int:
        an = 1
        k = 1
        l2r = True
        while n != 1:
            if l2r:
                an = an + k
                k = k * 2
                n = n // 2
                l2r = False
            else:
                if n % 2 == 1:
                    an = an + k
                k = k * 2
                n = n // 2
                l2r = True
        return an


if __name__ == "__main__":
    solution = Solution()
    print(solution.lastRemaining(9))
