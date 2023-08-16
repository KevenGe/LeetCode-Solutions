# 299. 猜数字游戏
# https://leetcode-cn.com/problems/bulls-and-cows/

################################################################################
from typing import Dict, Set


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d: Dict[str, Set[int]] = {}
        for i, s in enumerate(secret):
            if s in d:
                d[s].add(i)
            else:
                d[s] = set([i])

        dNum: Dict[str, int] = {}
        for k, v in d.items():
            dNum[k] = len(v)

        bullsNum = 0
        for i, s in enumerate(guess):
            if s in d and i in d[s]:
                bullsNum += 1
                dNum[s] -= 1

        cowsNum = 0
        for i, s in enumerate(guess):
            if s in d and i not in d[s] and dNum[s] > 0:
                dNum[s] -= 1
                cowsNum += 1

        return f"{str(bullsNum)}A{str(cowsNum)}B"


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(solution.getHint("1123", "0111"))

