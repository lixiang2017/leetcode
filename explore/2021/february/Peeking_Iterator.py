'''

You are here!
Your runtime beats 94.64 % of python submissions.
You are here!
Your memory usage beats 69.64 % of python submissions.
'''


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
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

class PeekingIterator(object):
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
        if not self.peek_num:
            return self.it.next()
        backup = self.peek_num
        self.peek_num = None
        return backup
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_num:
            return True
        return self.it.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
