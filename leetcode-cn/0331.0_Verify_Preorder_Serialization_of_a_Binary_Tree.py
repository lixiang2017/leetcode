'''
approach: Stack

执行用时：36 ms, 在所有 Python 提交中击败了17.54%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []

        for node in preorder.split(','):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')

        return 1 == len(stack) and stack[-1] == '#'

