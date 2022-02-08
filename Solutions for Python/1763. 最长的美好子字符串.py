# 1763. 最长的美好子字符串
# https://leetcode-cn.com/problems/longest-nice-substring/


class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        maxLen = 0
        maxStart = 0
        for left in range(len(s)):
            se = set()
            for right in range(left, len(s)):
                se.add(s[right])

                isOk = True
                for k in se:
                    if not ((k.islower() and k.upper() in se ) or (k.isupper() and k.lower() in se)):
                        isOk = False
                        break
                if isOk:
                    if right - left + 1 > maxLen:
                        maxLen = right - left + 1
                        maxStart = left

        return s[maxStart:maxStart+maxLen]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestNiceSubstring("YazaAay"))
