# 1996. 游戏中弱角色的数量
# https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/

from typing import List
from functools import cmp_to_key


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                return -(a[1] - b[1])

        properties.sort(key=cmp_to_key(cmp))

        count = 0
        max_i = properties[-1][:]
        for i in range(len(properties) - 1, -1, -1):
            if properties[i][0] < max_i[0]:
                if properties[i][1] < max_i[1]:
                    count += 1
                else:
                    max_i = properties[i][:]
            else:
                max_i = properties[i][:]

        return count


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.numberOfWeakCharacters(
            [[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]
        )
    )
