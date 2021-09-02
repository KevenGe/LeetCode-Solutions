# 150. 逆波兰表达式求值
# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                r = st.pop()
                l = st.pop()
                t = l + r
                st.append(t)
            elif token == "-":
                r = st.pop()
                l = st.pop()
                t = l - r
                st.append(t)
            elif token == "*":
                r = st.pop()
                l = st.pop()
                t = r * l
                st.append(t)
            elif token == "/":
                r = st.pop()
                l = st.pop()
                t = l / r
                if t > 0:
                    t = math.floor(t)
                else:
                    t = math.ceil(t)
                st.append(t)
            else:
                st.append(int(token))
        return st[0]


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )

