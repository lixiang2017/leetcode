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
