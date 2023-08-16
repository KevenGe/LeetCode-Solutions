# 面试题 03.01. 三合一
# https://leetcode-cn.com/problems/three-in-one-lcci/


class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = [0] * stackSize * 3
        self.stack_top = [0, 0 + stackSize, 0 + stackSize * 2]
        self.stack_bottom = [0, 0 + stackSize, 0 + stackSize * 2, 0 + stackSize * 3]

    def push(self, stackNum: int, value: int) -> None:
        if self.stack_top[stackNum] < self.stack_bottom[stackNum + 1]:
            self.stack[self.stack_top[stackNum]] = value
            self.stack_top[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.stack_top[stackNum] > self.stack_bottom[stackNum]:
            self.stack_top[stackNum] -= 1
            ans = self.stack[self.stack_top[stackNum]]
            return ans
        return -1

    def peek(self, stackNum: int) -> int:
        if self.stack_top[stackNum] > self.stack_bottom[stackNum]:
            ans = self.stack[self.stack_top[stackNum] - 1]
            return ans
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.stack_top[stackNum] == self.stack_bottom[stackNum]

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)

if __name__ == '__main__':
    s = TripleInOne(1)
    s.push(0,1)
    s.push(0,2)
    print(s.pop(0))
    print(s.pop(0))
    print(s.pop(0))