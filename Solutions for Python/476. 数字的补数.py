# 476. 数字的补数
# https://leetcode-cn.com/problems/number-complement/

################################################################################


class Solution:
    def findComplement(self, num: int) -> int:
        hi = 0
        for i in range(1, 32):
            t = 1 << i
            if num & t:
                hi = i
        mask = (1 << (hi + 1)) - 1
        return num ^ mask


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.findComplement(1))
