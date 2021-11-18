# 47. 全排列 II
# https://leetcode-cn.com/problems/permutations-ii/

################################################################################

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dp = [False for i in range(len(nums))]
        ans = []

        def dfs(index, dp, tmp, ans):
            if index == len(nums):
                ans.append(tmp.copy())

            for i in range(len(nums)):
                if dp[i] == False and (
                    (
                        i >= 1
                        and (
                            (nums[i - 1] == nums[i] and dp[i - 1])
                            or nums[i - 1] != nums[i]
                        )
                    )
                    or (i == 0)
                ):
                    dp[i] = True
                    tmp.append(nums[i])

                    dfs(index + 1, dp, tmp, ans)

                    tmp.pop()
                    dp[i] = False

        dfs(0, dp, [], ans)
        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))

