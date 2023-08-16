# 393. UTF-8 编码验证
# https://leetcode-cn.com/problems/utf-8-validation/


from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def get_one_before_zero(num: int):
            n = bin(num)
            n = "{:0>8}".format(n[2:])
            ans = 0
            for i in range(8):
                if n[i] == "0":
                    break
                else:
                    ans += 1
            return ans

        def is01(num: int):
            n = bin(num)
            n = "{:0>8}".format(n[2:])
            return n.startswith("10")

        n = -1
        for i in range(len(data)):
            if n == -1:
                n = get_one_before_zero(data[i])
                if n > 4:
                    break
                n = n - 1
            else:
                if not is01(data[i]):
                    break
                n = n - 1
                if n == 0:
                    n = -1

        return n == -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.validUtf8([250,145,145,145,145]))
