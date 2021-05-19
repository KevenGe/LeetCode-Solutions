"""

题目：338. 比特位计数

https://leetcode-cn.com/problems/counting-bits/
https://leetcode-cn.com/problems/counting-bits/
https://leetcode-cn.com/problems/counting-bits/

"""

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        
        if num == 0:
            return [0]
        elif num == 1:
            return [0,1]

        ans = [0 for _ in range(num+1)]
        ans[0] = 0
        ans[1] = 1

        offset = 2
        for i in range(2, num+1, 1):
            if i - offset == offset:
                offset = i

            ans[i] = ans[i-offset] + 1
        return ans
