# 1576. 替换所有的问号
# https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/


class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] == '?':
                for b in "abc":
                    if not (i > 0 and res[i - 1] == b or i < n - 1 and res[i + 1] == b):
                        res[i] = b
                        break
        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.modifyString("?zd"))