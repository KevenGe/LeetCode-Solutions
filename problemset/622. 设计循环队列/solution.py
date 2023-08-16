# 622. 设计循环队列
# https://leetcode.cn/problems/design-circular-queue/


class MyCircularQueue:
    def __init__(self, k: int):
        self.list = [0] * k
        self.first_idx = 0
        self.end_idx = 0
        self.size = 0
        self.max_size = k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False

        self.list[self.end_idx] = value
        self.end_idx = (self.end_idx + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        self.first_idx = (self.first_idx + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1

        return self.list[self.first_idx]

    def Rear(self) -> int:
        if self.size == 0:
            return -1

        return self.list[(self.end_idx + self.k - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
