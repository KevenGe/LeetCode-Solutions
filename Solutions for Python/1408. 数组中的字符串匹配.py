# 1408. 数组中的字符串匹配
# https://leetcode.cn/problems/string-matching-in-an-array/


from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            for word2 in words:
                if word != word2 and word in word2:
                    ans.append(word)
                    break
        return ans
