# 720. 词典中最长的单词
# https://leetcode-cn.com/problems/longest-word-in-dictionary/

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest
