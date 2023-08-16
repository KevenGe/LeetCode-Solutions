# 500. 键盘行
# https://leetcode-cn.com/problems/keyboard-row/

################################################################################
from typing import List
from functools import reduce


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = [set(list("qwertyuiop")), set(list("asdfghjkl")), set(list("zxcvbnm"))]

        def isOk(word: str) -> bool:
            isOK = True
            level = -1
            for i in range(len(word)):
                if level == -1:
                    for j in range(3):
                        if word[i].lower() in a[j]:
                            level = j
                            break
                else:
                    if word[i].lower() not in a[level]:
                        isOK = False
                        break
            return isOK

        def helper(x, y):
            if isOk(y):
                x.append(y)
            return x

        ans = reduce(helper, words, [])
        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
