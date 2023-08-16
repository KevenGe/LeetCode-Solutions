# 面试题 03.06. 动物收容所
# https://leetcode-cn.com/problems/animal-shelter-lcci/

from typing import List
from collections import deque

class AnimalShelf:

    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.last_index = 0

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cat_queue.append((animal[0], self.last_index))
        else:
            self.dog_queue.append((animal[0], self.last_index))
        self.last_index += 1

    def dequeueAny(self) -> List[int]:
        if len(self.dog_queue) == 0:
            if len(self.cat_queue) == 0:
                return [-1, -1]
            else:
                return self.dequeueCat()
        else:
            if len(self.cat_queue) == 0:
                return self.dequeueDog()
            else:
                if self.dog_queue[0][1] < self.cat_queue[0][1]:
                    return self.dequeueDog()
                else:
                    return self.dequeueCat()

    def dequeueDog(self) -> List[int]:
        if len(self.dog_queue) == 0:
            return [-1, -1]
        return [self.dog_queue.popleft()[0], 1]


    def dequeueCat(self) -> List[int]:
        if len(self.cat_queue) == 0:
            return [-1, -1]
        return [self.cat_queue.popleft()[0], 0]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()