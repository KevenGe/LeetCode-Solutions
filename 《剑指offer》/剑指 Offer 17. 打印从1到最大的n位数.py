# 剑指 Offer 17. 打印从1到最大的n位数
# https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        ans = []
        for i in range(10**n):
            ans.append(i)
        ans.pop(0)
        return ans


if __name__ == '__main__':
    solution = Solution()
