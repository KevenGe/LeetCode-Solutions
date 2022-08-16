# 641. 设计循环双端队列
# https://leetcode.cn/problems/design-circular-deque/


from typing import Union


class Node:
    def __init__(self, val=-1) -> None:
        self.val: int = val
        self.prior: Union[Node, None] = None
        self.next: Union[Node, None] = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.head: Node = Node()
        self.tail: Node = Node()
        self.size = 0

        self.head.next = self.tail
        self.tail.prior = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        m = Node(value)

        h = self.head
        t = self.head.next

        if t is None:
            raise Exception("")

        h.next = m
        m.prior = h

        t.prior = m
        m.next = t

        self.size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        m = Node(value)

        h = self.tail.prior
        t = self.tail

        if h is None:
            raise Exception("")

        h.next = m
        m.prior = h

        t.prior = m
        m.next = t

        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        h = self.head
        m = self.head.next
        t = self.head.next.next

        h.next = t
        t.prior = h

        self.size -= 1

        del m
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        h = self.tail.prior.prior
        m = self.tail.prior
        t = self.tail

        h.next = t
        t.prior = h

        self.size -= 1

        del m
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.prior.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


if __name__ == "__main__":
    m = MyCircularDeque(3)
    m.insertLast(1)
    m.insertLast(2)
    m.insertFront(3)
    m.insertFront(4)

    print(m.getRear())
    print(m.isFull())
    m.deleteLast()
    m.insertFront(4)
    print(m.getFront())
