'''
approach: Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 86.50 % of python submissions.
You are here!
Your memory usage beats 91.98 % of python submissions.
'''


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        while pushed and popped:     
            while pushed and (not stack or stack[-1] != popped[0]):
                stack.append(pushed.pop(0))
            while stack and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
        
        return not pushed and not popped




'''
approach: Stack
Time: O(N)
Space: O(N)

Runtime: 60 ms, faster than 42.47% of Python online submissions for Validate Stack Sequences.
Memory Usage: 13.4 MB, less than 99.22% of Python online submissions for Validate Stack Sequences.
'''

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack
    