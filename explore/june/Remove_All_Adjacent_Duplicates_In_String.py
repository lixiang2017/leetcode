'''
approach: Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 77.58 % of python3 submissions.
You are here!
Your memory usage beats 22.34 % of python3 submissions.
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        
        return ''.join(stack)



'''
Hash Set

You are here!
Your runtime beats 99.30 % of python3 submissions.
You are here!
Your memory usage beats 91.50 % of python3 submissions.
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        dup = {2 * ch for ch in set(s)}
        l = -1
        while l != len(s):
            l = len(s)
            for d in dup:
                s = s.replace(d, '')
        
        return s


'''
Hash Set

You are here!
Your runtime beats 99.83 % of python3 submissions.
You are here!
Your memory usage beats 81.74 % of python3 submissions.
'''
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        duplicates = [2 * ch for ch in ascii_lowercase]
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, '')
        return s
        