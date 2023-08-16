# 剑指 Offer 14- I. 剪绳子
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/


class Solution:
    def cuttingRope(self, n: int) -> int:
        a,b = divmod(n,3)
        if b == 0:
            if a == 1:
                return 2
            else:
                b = 1
        elif b == 1:
            a -= 1
            b = 2 * 2
        elif b == 2:
            if a == 0:
                return 1
        return (3 ** a) * b 


if __name__ == "__main__":
    so = Solution()
    print(so.cuttingRope(6))