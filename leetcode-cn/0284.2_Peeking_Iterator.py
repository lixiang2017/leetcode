'''
执行用时：32 ms, 在所有 Python3 提交中击败了74.88% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了59.61% 的用户
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
        self.peek_num = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peek_num:
            self.peek_num = self.it.next()
        return self.peek_num

    def next(self):
        """
        :rtype: int
        """
        if self.peek_num == None:
            return self.it.next()
        p = self.peek_num
        self.peek_num = None
        return p

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_num != None:
            return True
        return self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
