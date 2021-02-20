'''
approach: Stack
Time: O(N + NlogN + N) = O(NlogN)
Space: O(N)

You are here!
Your runtime beats 15.72 % of python submissions.
You are here!
Your memory usage beats 94.71 % of python submissions.
'''

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        missed = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop(-1)
                else:
                    missed.append(i)
        
        remove = sorted(stack + missed)
        valid = ''
        for i, ch in enumerate(s):
            if i not in remove:
                valid += ch
        return valid


'''
approach: Stack + Hash Table
Time: O(N + N + N) = O(N)
Space: O(N + N + N) = O(N)


You are here!
Your runtime beats 33.14 % of python submissions.
You are here!
Your memory usage beats 97.96 % of python submissions.
'''

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remove = {}
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop(-1)
                else:
                    remove[i] = 1
        
        for i in stack:
            remove[i] = 1
            
        valid = ''
        for i, ch in enumerate(s):
            if i not in remove:
                valid += ch
        return valid
    