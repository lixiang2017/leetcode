'''
approach: Monotone Increasing Stack
Time: O(N), the length of num
Space: O(N)

Success
Details 
Runtime: 28 ms, faster than 75.74% of Python online submissions for Remove K Digits.
Memory Usage: 13.8 MB, less than 79.02% of Python online submissions for Remove K Digits.
'''



class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack  = []
        
        for char in num:
            while stack and ord(stack[-1]) > ord(char) and k:
                stack.pop()
                k -= 1
            stack.append(char)
        
        while k:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == '0':
            stack.pop(0)

        return '0' if not stack else ''.join(stack)

'''
approach: Monotone Increasing Stack
Time: O(N), the length of num
Space: O(N)

Runtime: 36 ms, faster than 93.59% of Python3 online submissions for Remove K Digits.
Memory Usage: 14 MB, less than 93.92% of Python3 online submissions for Remove K Digits.
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        
        if k > 0:
            stack = stack[: -k]
        
        return ''.join(stack).lstrip('0') or '0'

