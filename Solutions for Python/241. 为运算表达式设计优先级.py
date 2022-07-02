# 241. 为运算表达式设计优先级
# https://leetcode.cn/problems/different-ways-to-add-parentheses/

from typing import List
from functools import lru_cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expressions = []

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                t = int(expression[i])
                i = i + 1
                while i < len(expression) and expression[i].isdigit():
                    t = t * 10 + int(expression[i])
                    i = i + 1
                expressions.append(t)
            else:
                expressions.append(expression[i])
                i = i + 1

        @lru_cache(2**len(expressions))
        def dfs(l: int, r: int) -> List[int]:
            if l > r:
                return []

            if l == r:
                return [expressions[l]]

            ans = []
            for i in range(l + 1, r, 2):
                left = dfs(l, i - 1)
                right = dfs(i + 1, r)

                if expressions[i] == "-":
                    for left_v in left:
                        for right_v in right:
                            ans.append(left_v - right_v)
                elif expressions[i] == "+":
                    for left_v in left:
                        for right_v in right:
                            ans.append(left_v + right_v)
                elif expressions[i] == "*":
                    for left_v in left:
                        for right_v in right:
                            ans.append(left_v * right_v)
            return ans

        return dfs(0, len(expressions) - 1)


if __name__ == "__main__":
    so = Solution()
    print(so.diffWaysToCompute("2-1-1"))
