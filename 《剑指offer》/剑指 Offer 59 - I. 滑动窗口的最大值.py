# 剑指 Offer 59 - I. 滑动窗口的最大值
# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        q = []
        for i in range(0, k):
            if len(q) == 0:
                q.append(nums[i])
            else:
                while len(q) > 0 and nums[i] > q[-1]:
                    q.pop()
                q.append(nums[i])

        ans = [q[0]]
        for i in range(k, len(nums)):
            lt = nums[i - k]
            if lt == q[0]:
                q.pop(0)

            while len(q) > 0 and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

