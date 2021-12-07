# 面试题 03.03. 堆盘子
# https://leetcode-cn.com/problems/stack-of-plates-lcci/


class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.cap:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        if len(self.stacks) == 0:
            return -1

        t = self.stacks[-1][-1]
        self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return t

    def popAt(self, index: int) -> int:
        if index >= len(self.stacks) or len(self.stacks) == 0:
            return -1
        t = self.stacks[index][-1]
        self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        return t

# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
