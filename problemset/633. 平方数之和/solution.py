from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))

        while a < b:
            n = a ** 2 + b ** 2
            if n == c:
                return True
            elif n < c:
                a += 1
            else:
                b -= 1

        return False
