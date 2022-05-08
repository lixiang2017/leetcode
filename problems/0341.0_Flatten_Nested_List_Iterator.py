'''
DFS

Runtime: 78 ms, faster than 63.93% of Python3 online submissions for Flatten Nested List Iterator.
Memory Usage: 17.9 MB, less than 41.16% of Python3 online submissions for Flatten Nested List Iterator.
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nl = nestedList
        self.arr = self.dfs(self.nl)
        self._next = next(self.arr, None)
        
    def dfs(self, nl):
        for nli in nl:
            if nli.isInteger():
                yield nli.getInteger()
            else:
                nll = nli.getList()
                yield from self.dfs(nll) 
    
    def next(self) -> int:
        x, self._next = self._next, next(self.arr, None)
        return x
    
    def hasNext(self) -> bool:
        return self._next is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

