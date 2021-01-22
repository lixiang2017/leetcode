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
    