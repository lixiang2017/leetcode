'''
You are here!
Your runtime beats 91.93 % of python submissions.
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
        self.flatten_this_list = list(reversed(list(self.flatten(nestedList))))

    def next(self):
        """
        :rtype: int
        """
        return self.flatten_this_list.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.flatten_this_list)
        
    def flatten(self, nestedList):
    	for ni_outer in nestedList:
    		if not ni_outer.isInteger():
    			for ni_inner in self.flatten(ni_outer.getList()): yield ni_inner
    		else: yield ni_outer.getInteger()

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
# Input: [[1,1],2,[1,1]]
	# Output: [1,1,2,1,1]
	# Explanation: By calling next repeatedly until hasNext returns false, 
	#             the order of elements returned by next should be: [1,1,2,1,1].
	nestedList = [[1,1],2,[1,1]]
	i, v = NestedIterator(nestedList), []
	while i.hasNext(): v.append(i.next())
	print v

	# Input: [1,[4,[6]]]
	#Output: [1,4,6]
	# Explanation: By calling next repeatedly until hasNext returns false, 
	#             the order of elements returned by next should be: [1,4,6].
	nestedList = [1,[4,[6]]]
	i, v = NestedIterator(nestedList), []
	while i.hasNext(): v.append(i.next())
	print v
