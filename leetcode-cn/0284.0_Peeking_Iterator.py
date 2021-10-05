'''
执行用时：24 ms, 在所有 Python3 提交中击败了97.54% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.42% 的用户
通过测试用例：14 / 14
'''

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
        self.it = iterator
        self.nums = []
        while self.it.hasNext():
            self.nums.append(self.it.next())
        self.idx = 0
        self.N = len(self.nums)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.idx]

    def next(self):
        """
        :rtype: int
        """
        x = self.nums[self.idx]
        self.idx += 1
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < self.N

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
