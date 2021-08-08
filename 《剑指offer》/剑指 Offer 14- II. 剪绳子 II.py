# 剑指 Offer 14- II. 剪绳子 II
# https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/


class Solution:
    def cuttingRope(self, n: int) -> int:
        a, b = divmod(n, 3)


        if a == 0:
            return 1
        elif a == 1:
            if b == 0:
                return 2
        
        if b == 1:
            a -= 1
            b = 4

        ans =  1 if b == 0 else b
        for i in range(a):
            ans = (ans * 3) % 1000000007

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.cuttingRope(8))
