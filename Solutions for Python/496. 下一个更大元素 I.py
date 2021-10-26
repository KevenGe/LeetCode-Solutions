# 496. 下一个更大元素 I
# https://leetcode-cn.com/problems/next-greater-element-i/

################################################################################

from typing import List
from functools import reduce


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stacks = []
        dDict = {}
        for n in reversed(nums2):
            if len(stacks) == 0:
                stacks.append(n)
                dDict[n] = -1
            else:
                if n < stacks[-1]:
                    dDict[n] = stacks[-1]
                    stacks.append(n)
                else:
                    while len(stacks) > 0 and n >= stacks[-1]:
                        stacks.pop()

                    if len(stacks) == 0:
                        dDict[n] = -1
                    else:
                        dDict[n] = stacks[-1]
                    stacks.append(n)

        ans = list(map(lambda x: dDict[x], nums1))
        return ans


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print([] == False)
    print([] == False)
    print([] is False)
