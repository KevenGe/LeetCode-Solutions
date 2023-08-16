# 面试题 05.04. 下一个数
# https://leetcode.cn/problems/closed-number-lcci/

from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:

        max_num = 2147483647

        bigger_num = -1
        lower_num = -1

        for i in range(30):
            if (num & (1 << i) != 0) and (num & (1 << (i + 1)) == 0):
                bigger_num = num - 2 ** i + 2 ** (i + 1)

                one_s = 0
                for one_i in range(i-1, -1, -1):
                    if num & (1 << one_i):
                        bigger_num = bigger_num - 2 ** one_i + 2 ** one_s
                        one_s += 1
                    else:
                        break

                break

        for i in range(32):
            if (num & (1 << i) == 0) and (num & (1 << (i + 1)) != 0):
                lower_num = num + 2 ** i - 2 ** (i + 1)

                one_s = i - 1
                for one_i in range(i):
                    if num & (1 << one_i):
                        lower_num = lower_num - 2 ** one_i + 2 ** one_s
                        one_s -= 1
                    else:
                        break
                break

        return [bigger_num, lower_num]


if __name__ == "__main__":
    so  =Solution()
    print(so.findClosedNumbers(2147483647))
