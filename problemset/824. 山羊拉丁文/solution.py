# 824. 山羊拉丁文
# https://leetcode-cn.com/problems/goat-latin/

from functools import reduce


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        new_words = []
        for i, word in enumerate(words, 1):
            
            if word[0] in "AEIOUaeiou":
                new_word = word + "ma"
            else:
                new_word = word[1:]+word[0]+"ma"
            new_word = new_word + "a" * i
            new_words.append(new_word)
        new_sentence = " ".join(new_words)
        return new_sentence
