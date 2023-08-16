# 736. Lisp 语法解析
# https://leetcode.cn/problems/parse-lisp-expression/

from typing import List, Dict


class Solution:
    def evaluate(self, expression: str) -> int:
        def par(expression: str) -> List[str]:
            expression = expression[1:-1]
            exps = expression.split(" ")
            ans: List[str] = []

            i = 0
            while i < len(exps):
                if exps[i].__contains__("("):
                    left_bracket_count = 0
                    for z in range(i, len(exps)):
                        left_bracket_count = (
                            left_bracket_count + exps[z].count("(") - exps[z].count(")")
                        )
                        if left_bracket_count == 0:
                            ans.append(" ".join(exps[i : z + 1]))
                            i = z + 1
                            break
                else:
                    ans.append(exps[i])
                    i = i + 1

            return ans

        def ev(expression: str, data: Dict[str, int]) -> int:
            if not expression.startswith("("):
                if expression.isdigit() or (
                    expression[0] == "-" and expression[1:].isdigit()
                ):
                    return int(expression)
                else:
                    return data[expression]

            if expression.startswith("(let"):
                exps = par(expression)
                data = data.copy()
                for i in range(1, len(exps), 2):
                    if i + 1 >= len(exps):
                        return ev(exps[-1], data)
                    data[exps[i]] = ev(exps[i + 1], data)

            elif expression.startswith("(add"):
                exps = par(expression)
                return ev(exps[1], data) + ev(exps[2], data)
            elif expression.startswith("(mult"):
                exps = par(expression)
                return ev(exps[1], data) * ev(exps[2], data)

        return ev(expression, dict())


if __name__ == "__main__":
    so = Solution()
    # assert so.evaluate("(let x 3 x 2 x)") == 2, "1"
    # assert so.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))") == 14, "2"
    # print(so.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))
    assert so.evaluate("(let x 1 y 2 x (add x y) (add x y))") == 5, "3"
    assert so.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))") == 6
    print(so.evaluate("(let a1 3 b2 (add a1 1) b2)"))
    assert so.evaluate("(let x 7 -12)") == -12
