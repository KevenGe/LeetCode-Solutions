# 640. 求解方程
# https://leetcode.cn/problems/solve-the-equation/

from typing import Tuple


class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(equation: str) -> Tuple[int, int]:
            x1 = 0
            x0 = 0

            item_start_idx = 0
            item_exp = "+"
            get_eq = False
            for i in range(len(equation)):
                if equation[i] in ["+", "-", "="]:
                    if i - item_start_idx == 0:
                        item_start_idx = i + 1
                        item_exp = equation[i]
                        continue

                    item = equation[item_start_idx:i]
                    item_start_idx = i + 1
                    if "x" in item:
                        if len(item[:-1]) == 0:
                            item_val = 1
                        else:
                            item_val = int(item[:-1])

                        if (item_exp == "+") ^ get_eq:
                            x1 += item_val
                        else:
                            x1 -= item_val
                    else:
                        if (item_exp == "+") ^ get_eq:
                            x0 += int(item)
                        else:
                            x0 -= int(item)

                    if equation[i] == "=":
                        get_eq = True
                        item_exp = "+"
                    else:
                        item_exp = equation[i]

            item = equation[item_start_idx:]
            if "x" in item:
                if len(item[:-1]) == 0:
                    item_val = 1
                else:
                    item_val = int(item[:-1])

                if (item_exp == "+") ^ get_eq:
                    x1 += item_val
                else:
                    x1 -= item_val
            else:
                if (item_exp == "+") ^ get_eq:
                    x0 += int(item)
                else:
                    x0 -= int(item)

            return x1, x0

        x1, x0 = parse(equation)

        if x1 == 0:
            if x0 == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={}".format(-x0 // x1)


if __name__ == "__main__":
    so = Solution()
    print(so.solveEquation("x+5-3+x=6+x-2"))
    print(so.solveEquation("x=x"))
    print(so.solveEquation("2x=x"))
    print(so.solveEquation("-x=-1"))
    print(so.solveEquation("-x=-345"))
    print(so.solveEquation("-x=-1"))
