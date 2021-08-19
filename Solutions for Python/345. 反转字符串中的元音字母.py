# 345. 反转字符串中的元音字母
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        def isYuanYin(s: str):
            s = s.lower()
            return s == "a" or s == "e" or s == "i" or s == "o" or s == "u"

        s = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and isYuanYin(s[l]) is False:
                l += 1

            while l < r and isYuanYin(s[r]) is False:
                r -= 1

            if l == r:
                break
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("HELLO"))
