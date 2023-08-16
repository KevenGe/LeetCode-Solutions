# 537. 复数乘法
# https://leetcode-cn.com/problems/complex-number-multiplication/
import re
from typing import Tuple


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def parser_complex(num:str)-> Tuple[int, int]:
            t = re.search("^(.*?)[+](.*?)i$", num)
            return int(t.group(1)), int(t.group(2))

        num1_a, num1_b = parser_complex(num1)
        num2_a, num2_b = parser_complex(num2)

        num3_a = num1_a * num2_a - num1_b * num2_b
        num3_b = num1_a * num2_b + num2_a * num1_b

        num3 = "{0}+{1}i".format(num3_a, num3_b)
        return num3


if __name__ == "__main__":
    solution = Solution()
    print(solution.complexNumberMultiply("1+1i", "1+1i"))

