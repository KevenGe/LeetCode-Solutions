# 2000. 反转单词前缀
# https://leetcode-cn.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_index = word.find(ch)
        if ch_index == -1:
            return word

        return  word[:ch_index+1][::-1] + word[ch_index + 1:]
