# 1455. 检查单词是否为句中其他单词的前缀
# https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/



class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return idx + 1
        return -1
