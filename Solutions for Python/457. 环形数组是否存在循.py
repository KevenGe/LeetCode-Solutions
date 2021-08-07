# 457. 环形数组是否存在循环
# https://leetcode-cn.com/problems/circular-array-loop/

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if visited[i] == False:
                
                newVisited = [False] * len(nums)

                t = i
                while True:
                    visited[t] = True
                    newVisited[t] = True
                    t2 = (t + nums[t] + len(nums)) % len(nums)
                    if t == t2:
                        break
                    t = t2

                    if newVisited[t] == True:

                        symbol = True
                        if nums[t] > 0:
                            symbol = True
                        elif nums[t] == 0:
                            break
                        else:
                            symbol = False

                        allTrue = True
                        t2 = (t + nums[t]) % len(nums)
                        while True:
                            if t2 == t:
                                break
                            elif symbol:
                                if nums[t2] <= 0:
                                    allTrue = False
                                    break
                            else:
                                if nums[t2] >= 0:
                                    allTrue = False
                                    break
                            t2 = (t2 + nums[t2]) % len(nums)
                        if allTrue:
                            return True
                        else:
                            break

        return False


def test_1():
    solution = Solution()
    print(solution.circularArrayLoop([-2,1,-1,-2,-2]))


if __name__ == "__main__":
    test_1()
