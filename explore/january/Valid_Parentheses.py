'''
approach: Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 68.21 % of python submissions.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        same = {'(': ')', '{': '}', '[': ']'}
        
        for letter in s:
            if letter in ['(', '{', '[']:
                stack.append(letter)
                continue
            else:
                if stack and same[stack[-1]] == letter:
                    stack.pop()
                    continue
                else:
                    return False
        
        return not stack
