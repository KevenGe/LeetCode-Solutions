# 441. 排列硬币
# https://leetcode-cn.com/problems/arranging-coins/

################################################################################


class Solution:
    def arrangeCoins(self, n: int) -> int:

        for level in range(1, 2 ** 33):
            n -= level
            if n < 0:
                return level - 1


################################################################################

if __name__ == "__main__":
    solution = Solution()

