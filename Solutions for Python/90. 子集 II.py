# 90. 子集 II
# https://leetcode-cn.com/problems/subsets-ii/

################################################################################
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False for i in range(len(nums))]

        def dfs(
            index: int, visited: List[bool], tmp: List[int], ans: List[List[int]]
        ) -> None:
            if index == len(nums):
                ans.append(tmp.copy())
                return

            if (
                index >= 1
                and visited[index - 1] == False
                and nums[index - 1] == nums[index]
            ):
                dfs(index + 1, visited, tmp, ans)
                return

            dfs(index + 1, visited, tmp, ans)

            tmp.append(nums[index])
            visited[index] = True
            dfs(index + 1, visited, tmp, ans)
            visited[index] = False
            tmp.pop()

        nums.sort()
        dfs(0, visited, [], ans)

        return ans


################################################################################


if __name__ == "__main__":
    solution = Solution()
