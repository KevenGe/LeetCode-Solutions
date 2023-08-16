# 5946. 句子中的最多单词数
# https://leetcode-cn.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len  = 0
        for sentence in sentences:
            max_len = max(max_len, len(sentence.split(" ")))
        return max_len
