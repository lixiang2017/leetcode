'''
approach: Split + Stack
Time: O(N + N) = O(N), where N is the length of path.
Space: O(N + N) = O(N)

You are here!
Your runtime beats 50.20 % of python submissions.
You are here!
Your memory usage beats 90.61 % of python submissions.
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        canonical = ''
        stack = []
        marks = path.split('/')
        for mark in marks:
            if mark == '' or mark == '.':
                continue
            elif mark == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(mark)
        
        return '/' + '/'.join(stack)
        