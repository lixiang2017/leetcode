'''
Hint 1
Each prefix of a balanced parentheses has a number of open parentheses greater
 or equal than closed parentheses, similar idea with each suffix.
Hint 2
Check the array from left to right, remove characters that do not meet 
the property mentioned above, same idea in backward way.

T: O(2N)
S: O(2N)
Runtime: 151 ms, faster than 55.75% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 17.9 MB, less than 5.42% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        # from left to right
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
                stack.append(ch)
            elif ch == ')':
                if left > 0:
                    left -= 1
                    stack.append(ch)
            else:
                stack.append(ch)
        
        # from right to left
        stack1 = []
        for ch in stack[::-1]:
            if ch == ')':
                right += 1
                stack1.append(ch)
            elif ch == '(':
                if right > 0:
                    right -= 1
                    stack1.append(ch)
            else:
                stack1.append(ch)
                
        return ''.join(stack1[:: -1])
    
