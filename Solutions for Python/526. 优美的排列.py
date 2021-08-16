# 526. 优美的排列
# https://leetcode-cn.com/problems/beautiful-arrangement/


class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            m = bin(mask).count("1")
            for j in range(1, n + 1):
                if mask & (1 << (j - 1)) and (m % j == 0 or j % m == 0):
                    f[mask] += f[mask ^ (1 << (j - 1))]
        return f[(1 << n) - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.countArrangement(5))
