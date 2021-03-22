'''
执行用时：68 ms, 在所有 Python 提交中击败了34.74%的用户
内存消耗：18.4 MB, 在所有 Python 提交中击败了97.89%的用户
'''


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested = nestedList
        self.flatten = self.flat(nestedList)
        self.N = len(self.flatten)
        self.ptr = 0

    def flat(self, nestedList):
        flatList = []
        for nested in nestedList:
            if nested.isInteger():
                flatList.append(nested.getInteger())
            else:
                flatList += self.flat(nested.getList())
        return flatList
        

    def next(self):
        """
        :rtype: int
        """
        nextvalue = self.flatten[self.ptr]
        self.ptr += 1
        return nextvalue

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ptr < self.N

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

