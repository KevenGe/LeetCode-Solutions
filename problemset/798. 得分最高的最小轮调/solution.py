# 798. 得分最高的最小轮调
# https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/


from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        cha = [0] * (len(nums)+1)
        n = len(nums)

        for i in range(len(nums)):
            x = nums[i]
            if i >= x:
                cha[0] += 1
                cha[i- x + 1] -= 1

                cha[i + 1] += 1
                cha[n] -= 1
            else:
                cha[i+1] += 1
                cha[i+n-x + 1] -= 1

        res = [0] * n
        res[0] = cha[0]
        for i in range(1, n):
            res[i] = res[i-1] + cha[i]

        maxI = -1
        maxK = -1
        for i in range(len(res)):
            if res[i] > maxK:
                maxK = res[i]
                maxI = i

        return maxI


if __name__ == "__main__":
    solution = Solution()
    print(solution.bestRotation([2,3,1,4,0]))
