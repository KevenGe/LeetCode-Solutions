# 面试题 10.02. 变位词组
# https://leetcode-cn.com/problems/group-anagrams-lcci/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nStrs = []
        for i in range(len(strs)):
            nStrs.append(("".join(sorted(strs[i])), strs[i]))
        nStrs = sorted(nStrs, key=lambda x: x[0])

        ans = []
        beforeStr = None

        for nStr in nStrs:
            if nStr[0] != beforeStr:
                ans.append([])
                ans[-1].append(nStr[1])
                beforeStr = nStr[0]
            else:
                ans[-1].append(nStr[1])

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

