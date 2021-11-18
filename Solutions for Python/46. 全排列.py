# 46. 全排列
# https://leetcode-cn.com/problems/permutations/

################################################################################
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        state = dict([(num, False) for num in nums])

        ans = []

        def dfs(index: int, state, tmp, ans):
            if index == len(nums):
                ans.append(tmp.copy())

            for k, v in state.items():
                if v == False:
                    state[k] = True
                    tmp.append(k)
                    dfs(index + 1, state, tmp, ans)
                    tmp.pop()
                    state[k] = False

        dfs(0, state, [], ans)
        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
