# 467. 环绕字符串中唯一的子字符串
# https://leetcode.cn/problems/unique-substrings-in-wraparound-string/


# class Solution:
#     def findSubstringInWraproundString(self, p: str) -> int:

#         isSub = [True] * len(p)
#         ans = len(set(p))

#         for p_len in range(2, len(p)+1):
#             cur_len_set = set()
#             for s in range(len(p) - p_len+1):
#                 if isSub[s]:
#                     if p[s+p_len-1] == chr((ord(p[s+p_len-2]) - ord('a') + 1) % 26 + ord('a')):
#                         cur_len_set.add(p[s:s+p_len])
#                     else:
#                         isSub[s] = False
#             ans += len(cur_len_set)
#         return ans


from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        de = defaultdict(int)

        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(p[i]) - ord(p[i-1]) + 25) % 26 == 0:
                k += 1
            else:
                k = 1
            de[ch] = max(de[ch], k)
        return sum(de.values())



if __name__ == "__main__":
    so = Solution()
    # print(so.findSubstringInWraproundString("a"))
    # print(so.findSubstringInWraproundString("cac"))
    print(so.findSubstringInWraproundString("abaab"))
