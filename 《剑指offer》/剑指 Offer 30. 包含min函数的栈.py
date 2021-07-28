# 剑指 Offer 30. 包含min函数的栈
# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stacks = []
        self.h = []

    def push(self, x: int) -> None:
        self.stacks.append(x)
        if len(self.h) == 0:
            self.h.append([x, len(self.stacks)])
        else:
            if self.h[-1][0] > x:
                self.h.append([x, len(self.stacks)])

    def pop(self) -> None:
        t = self.stacks[-1]
        if t == self.h[-1][0] and len(self.stacks) == self.h[-1][1]:
            self.h.pop()
        self.stacks.pop()

    def top(self) -> int:
        return self.stacks[-1]

    def min(self) -> int:
        return self.h[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
