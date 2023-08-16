# 面试题 03.05. 栈排序
# https://leetcode-cn.com/problems/sort-of-stacks-lcci/

class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
        else:
            tmp_stack = []
            while len(self.stack) != 0 and self.stack[-1] < val:
                tmp_stack.append(self.stack.pop())
            self.stack.append(val)
            while len(tmp_stack) != 0:
                self.stack.append(tmp_stack.pop())

    def pop(self) -> None:
        if self.isEmpty() is False:
            self.stack.pop()

    def peek(self) -> int:
        if self.isEmpty() is False:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
