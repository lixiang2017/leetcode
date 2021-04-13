'''
approach: Iterator

You are here!
Your runtime beats 99.58 % of python3 submissions.
You are here!
Your memory usage beats 89.70 % of python3 submissions.
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
        
        def generator(nodes):
            for node in nodes:
                if node.isInteger():
                    yield node.getInteger()
                else:
                    yield from generator(node.getList())
        
        self.it = generator(nestedList)
        self.value = next(self.it, None)
        
    
    def next(self) -> int:
        result = self.value
        self.value = next(self.it, None)
        return result
    
    def hasNext(self) -> bool:
        return self.value is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
