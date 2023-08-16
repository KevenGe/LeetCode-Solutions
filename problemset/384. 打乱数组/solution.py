# 384. 打乱数组
# https://leetcode-cn.com/problems/shuffle-an-array/

################################################################################

from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums.copy()

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        newNums = self.nums.copy()
        for i in range(len(newNums) - 1, 0, -1):
            t = random.randint(0, i)
            newNums[t], newNums[i] = newNums[i], newNums[t]
        return newNums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


################################################################################

if __name__ == "__main__":
    solution = Solution([1, 2, 3, 4, 5])
    print(solution.shuffle())
