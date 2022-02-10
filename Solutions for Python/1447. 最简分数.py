# 1447. 最简分数
# https://leetcode-cn.com/problems/simplified-fractions/


from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        def gcd(a, b):
            ans = 1
            for i in range(2, min(a, b)+1):
                if a % i == 0 and b % i == 0:
                    ans = i
                    break
            return ans

        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    ans.append("{0}/{1}".format(j, i))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifiedFractions(4))
