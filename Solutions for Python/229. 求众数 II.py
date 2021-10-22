# 229. 求众数 II
# https://leetcode-cn.com/problems/majority-element-ii/

################################################################################
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cou = Counter()
        for num in nums:
            cou[num] += 1

        ans = []
        for k, n in cou.most_common():
            if n > len(nums) // 3:
                ans.append(k)

        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))

