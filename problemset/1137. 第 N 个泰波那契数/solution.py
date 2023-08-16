# 1137. 第 N 个泰波那契数
# https://leetcode-cn.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        if n <= 2:
            return ans[n]

        for i in range(3, n + 1):
            ans.append(ans[i - 3] + ans[i - 2] + ans[i - 1])

        return ans[-1]


if __name__ == "__main__":
    pass
