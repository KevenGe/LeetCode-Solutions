# 171. Excel表列序号
# https://leetcode-cn.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for i, n in enumerate(reversed(columnTitle)):
            ans += (ord(n) - ord("A") + 1) * (26 ** i)

        return ans

if __name__ == "__main__":
    solution = Solution()
