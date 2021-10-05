# 284. 窥探迭代器
# https://leetcode-cn.com/problems/peeking-iterator/


################################################################################

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.num = []
        while iterator.hasNext():
            self.num.append(iterator.next())

        self.i = 0
        self.n = len(self.num)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.num[self.i]

    def next(self):
        """
        :rtype: int
        """
        t = self.num[self.i]
        self.i += 1
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i  < self.n


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

################################################################################


if __name__ == "__main__":
    solution = PeekingIterator()
