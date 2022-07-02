# LCP 30. 魔塔游戏
# https://leetcode.cn/problems/p0NxJO/

from typing import List
from queue import PriorityQueue


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        p = PriorityQueue()
        count = 0
        cur_life = 1
        sub_lift = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                cur_life += nums[i]
            else:
                cur_life += nums[i]

                if cur_life > 0:
                    p.put_nowait(nums[i])
                else:
                    p.put_nowait(nums[i])

                    t = p.get_nowait()
                    cur_life = cur_life + (-t)
                    sub_lift = sub_lift + t
                    count += 1

        cur_life += sub_lift

        if cur_life > 0:
            return count
        else:
            return -1


if __name__ == "__main__":
    so = Solution()
    print(so.magicTower([100, 100, 100, -250, -60, -140, -50, -50, 100, 150]) == 1)
