# 剑指 Offer 41. 数据流中的中位数
# https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/

import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []
        self.B = []

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heapq.heappush(self.A, -heapq.heappushpop(self.B, -num))
        else:
            heapq.heappush(self.B, -heapq.heappushpop(self.A, num))

    def findMedian(self) -> float:
        if len(self.A) == len(self.B):
            return (self.A[0] - self.B[0]) / 2
        else:
            return self.A[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    m = MedianFinder()
