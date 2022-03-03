# 77. 组合
# https://leetcode-cn.com/problems/combinations/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(start_idx: int, last_k:int) -> List[List[int]]:
            if last_k == 0:
                return []
            ans = []
            for i in range(start_idx, n - last_k + 1):
                ans2 = dfs(i + 1, last_k - 1)
                if len(ans2) == 0:
                    ans.append([i + 1])
                else:
                    for t in ans2:
                        ans.append([i + 1, *t])
            return ans

        ans = dfs(0, k)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(4,2))
