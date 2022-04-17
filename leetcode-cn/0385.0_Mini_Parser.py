'''
执行用时：56 ms, 在所有 Python3 提交中击败了80.28% 的用户
内存消耗：24.2 MB, 在所有 Python3 提交中击败了21.83% 的用户
通过测试用例：58 / 58
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

'''
[3, [4], [0, 5, 6, 0], 33, [-7, [8, [9], [-66]]], 10]
'''
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        return NestedInteger(eval(s))




'''
执行用时：52 ms, 在所有 Python3 提交中击败了87.32% 的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了57.04% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        num = ''
        for ch in s:
            match ch:
                case '[':
                    stack.append(NestedInteger())
                case ',' | ']':
                    if len(num):
                        # int() handles negative number
                        stack[-1].add(NestedInteger(int(num)))
                        num = ''
                    if ch == ']' and  len(stack) > 1:
                        ni = stack.pop()
                        stack[-1].add(ni)
                case _:
                    num += ch 
        
        return stack[0] if stack else NestedInteger(int(num))



