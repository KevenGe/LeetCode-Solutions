# 剑指 Offer 61. 扑克牌中的顺子
# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/

from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        any = 0
        for num in nums:
            if num == 0:
                any += 1
        
        start = -1
        for i in range(len(nums)):
            if nums[i] !=0 :
                if start == -1:
                    start = nums[i]
                else:
                    while nums[i] != start + 1: 
                        if any > 0:
                            any -= 1
                            start += 1
                        else:
                            return False
                    start += 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isStraight([1,2,0,6,5]))
