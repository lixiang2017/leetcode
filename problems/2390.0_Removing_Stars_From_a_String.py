'''
stack 

Runtime: 274 ms, faster than 38.71% of Python3 online submissions for Removing Stars From a String.
Memory Usage: 15.5 MB, less than 77.42% of Python3 online submissions for Removing Stars From a String.
'''
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                if stack and stack[-1] != '*':
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return ''.join(stack)
        