# 89. 格雷编码
# https://leetcode-cn.com/problems/gray-code/

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            t = len(ans)
            for j in range(t - 1, -1, -1):
                ans.append(ans[j] ^ (1 << i))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.grayCode(2))
