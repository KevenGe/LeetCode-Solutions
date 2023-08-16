# 292. Nim 游戏
# https://leetcode-cn.com/problems/nim-game/

################################################################################


class Solution:
    def canWinNim(self, n: int) -> bool:
        t = n % 4
        return t != 0


################################################################################


if __name__ == "__main__":
    solution = Solution()
