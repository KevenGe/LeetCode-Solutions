# 面试题 03.04. 化栈为队
# https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        quequ_stack_helper = []

        while len(self.queue_stack) != 0:
            quequ_stack_helper.append(self.queue_stack.pop())

        ans = quequ_stack_helper.pop()
        while len(quequ_stack_helper) != 0:
            self.queue_stack.append(quequ_stack_helper.pop())
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        quequ_stack_helper = []

        while len(self.queue_stack) != 0:
            quequ_stack_helper.append(self.queue_stack.pop())

        ans = quequ_stack_helper[-1]
        while len(quequ_stack_helper) != 0:
            self.queue_stack.append(quequ_stack_helper.pop())
        return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
