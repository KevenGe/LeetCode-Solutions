# 1705. 吃苹果的最大数目
# https://leetcode-cn.com/problems/maximum-number-of-eaten-apples/


from typing import List
import heapq

class Node:
    def __init__(self, apple, day):
        self.apple = apple
        self.day = day

    def __lt__(self, other):
        return self.day < other.day


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        nums = []
        heapq.heapify(nums)

        current_day = 0
        apple_num = 0
        while True:
            if current_day < len(apples):
                heapq.heappush(nums, Node(apples[current_day], days[current_day] + current_day))

            while len(nums)!=0 and (nums[0].day <= current_day or nums[0].apple == 0):
                heapq.heappop(nums)

            if len(nums) != 0:
                nums[0].apple -= 1
                apple_num += 1
            else:
                if current_day >= len(apples):
                    break

            current_day += 1

        return apple_num


if __name__ == '__main__':
    solution = Solution()
    print(solution.eatenApples([3,0,0,0,0,2], [3,0,0,0,0,2]))
