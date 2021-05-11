'''
approach: Stack
Time: O(N + N) = O(N)
Space: O(N + N) = O(N)

You are here!
Your runtime beats 63.51 % of python submissions.
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        match = [0] * N
        stack = []
        
        for i, token in enumerate(s):
            if '(' == token:
                stack.append((token, i))
            else: # ')'
                if stack and stack[-1][0] == '(':  # matched
                    match[i] = 1
                    match[stack[-1][1]] = 1
                    stack.pop()
                else: # not matched
                    stack.append((token, i))
        
        # find the longest 1s in match array
        from itertools import groupby
        lens = [len(list(group)) for key, group in groupby(match) if 1 == key]
        return max(lens) if lens else 0

