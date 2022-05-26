'''
stack
T: O(N)
S: O(N)

Runtime: 102 ms, faster than 9.40% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14.7 MB, less than 46.94% of Python3 online submissions for Longest Valid Parentheses.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, stack = 0, [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans 
    

'''
Input
"()(())"
Output
4
Expected
6
'''


'''
stack
T: O(2N)
S: O(1)

Runtime: 86 ms, faster than 17.53% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14 MB, less than 91.28% of Python3 online submissions for Longest Valid Parentheses.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, n = 0, len(s)
        left = right = 0
        for i, ch in enumerate(s):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, right * 2)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, left * 2)
            elif left > right:
                left = right = 0
        
        return ans 
        
