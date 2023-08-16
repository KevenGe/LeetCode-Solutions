# 717. 1比特与2比特字符
# https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        last_bit = -1
        idx = 0
        while idx < len(bits):
            if bits[idx] == 0:
                idx += 1
                last_bit = 1
            else:
                idx += 2
                last_bit = 2

        if last_bit == 1:
            return True
        else:
            return False
