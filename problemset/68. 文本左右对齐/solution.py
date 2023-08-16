# 68. 文本左右对齐
# https://leetcode-cn.com/problems/text-justification/


################################################################################
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        l = 0
        while l < len(words):
            lens = len(words[l])

            r = l

            while lens <= maxWidth and r + 1 < len(words):
                if lens + len(words[r + 1]) + 1 <= maxWidth:
                    lens += len(words[r + 1]) + 1
                    r += 1
                else:
                    break

            t = ""
            if r - l == 0 or r == len(words) - 1:
                t = words[l]
                for i in range(l + 1, r + 1):
                    t += " " + words[i]
                t += (maxWidth - len(t)) * " "
            else:
                whiteSpaceLen = maxWidth - (lens - (r - l))
                whiteSpaceList = [" " * (whiteSpaceLen // (r - l))] * (r - l)
                for i in range(whiteSpaceLen % (r - l)):
                    whiteSpaceList[i] += " "

                t = words[l]
                for i in range(r - l):
                    t += whiteSpaceList[i] + words[l + i + 1]

            ans.append(t)
            l = r + 1
        return ans


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
    )
