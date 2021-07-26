# 剑指 Offer 15. 二进制中1的个数
# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
