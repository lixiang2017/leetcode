'''
stack
T: O(N)
S: O(N)

Runtime: 66 ms, faster than 58.17% of Python3 online submissions for Make The String Great.
Memory Usage: 14 MB, less than 15.06% of Python3 online submissions for Make The String Great.
'''
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ord(stack[-1]) ^ 32 == ord(ch):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        
