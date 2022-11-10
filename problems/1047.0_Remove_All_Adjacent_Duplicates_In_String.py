'''
stack
T: O(N)
S: O(N)

Runtime: 176 ms, faster than 54.54% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 14.8 MB, less than 86.70% of Python3 online submissions for Remove All Adjacent Duplicates In String.
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
