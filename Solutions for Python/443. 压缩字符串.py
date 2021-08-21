# 443. 压缩字符串
# https://leetcode-cn.com/problems/string-compression/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        beforeChar = chars[0]
        beforeNum = 0
        left = 0
        chars.append("@@@")
        for j, c in enumerate(chars):
            if c == beforeChar:
                beforeNum = beforeNum + 1
            else:
                if beforeNum != 1:
                    chars[left] = beforeChar
                    beforeChar = c

                    left += 1
                    beforeNumStr = str(beforeNum)
                    for i in range(len(beforeNumStr)):
                        chars[left + i] = beforeNumStr[i]

                    left += len(beforeNumStr)
                    beforeNum = 1
                else:
                    chars[left] = beforeChar
                    left += 1
                    beforeChar = c

        while left + 1 <= len(chars):
            chars.pop()

        # print(chars)
        return len(chars)


if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a", "b", "b"]))
