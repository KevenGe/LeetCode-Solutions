# 295. 数据流的中位数
# https://leetcode-cn.com/problems/find-median-from-data-stream/
import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []  # 小根堆，n/2+1
        self.b = []  # 大根堆, n/2

    def addNum(self, num: int) -> None:
        if len(self.a) == 0:
            self.a.append(num)
            return

        if len(self.a) == len(self.b):
            if num < self.a[0]:
                t = -heapq.heappushpop(self.b, -num)
                heapq.heappush(self.a, t)
            else:
                heapq.heappush(self.a, num)
        else:
            t = heapq.heappushpop(self.a, num)
            heapq.heappush(self.b, -t)

    def findMedian(self) -> float:
        if len(self.a) == len(self.b):
            return (self.a[0] - self.b[0]) / 2
        else:
            return self.a[0]


if __name__ == "__main__":
    m = MedianFinder()
    m.addNum(-1)
    m.addNum(-2)
    m.addNum(-3)
    print(m.findMedian())
