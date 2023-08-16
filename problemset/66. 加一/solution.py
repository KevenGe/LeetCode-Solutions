# 66. 加一
# https://leetcode-cn.com/problems/plus-one/

################################################################################
# from typing import List


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         return list(
#             map(
#                 lambda x: int(x),
#                 list(str(int("".join(map(lambda x: str(x), digits))) + 1)),
#             )
#         )
################################################################################
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + add
            if digits[i] == 10:
                digits[i] = 0
                add = 1
            else:
                add = 0
                break
        if add:
            digits.insert(0, 1)

        return digits


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))

