# 881. 救生艇
# https://leetcode-cn.com/problems/boats-to-save-people/

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
