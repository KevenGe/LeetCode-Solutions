# 371. 两整数之和
# https://leetcode-cn.com/problems/sum-of-two-integers/

################################################################################


class Solution:
    def getSum(self, a: int, b: int) -> int:

        MASK1 = 4294967296  # 2^32
        MASK2 = 2147483648  # 2^31
        MASK3 = 2147483647  # 2^31-1

        m = a
        n = b
        while n != 0:
            t = ((m&n) << 1) % MASK1
            m = (m^n) % MASK1
            n = t
        
        if m & MASK2:  # 负数
            return ~((m ^ MASK2) ^ MASK3)
        else:  # 正数
            return m


################################################################################

if __name__ == "__main__":
    solution = Solution()

    print(-2 & 1)
    print(-2 & 2)
    print(-2 & 4)

