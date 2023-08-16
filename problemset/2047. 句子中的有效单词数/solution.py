# 2047. 句子中的有效单词数
# https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/


################################################################################

from functools import reduce
import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def isOk(word: str) -> bool:
            ans = re.match(
                "^(([a-z]*(([a-z]\-[a-z])|[a-z])[a-z]*[\!\.,]?)|[\!\.,])$", word
            )
            return ans is not None

        t = reduce(lambda x, y: x + (1 if isOk(y) else 0), sentence.split(" "), 0)
        return t


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(solution.countValidWords("alice and  bob are playing stone-game10"))
