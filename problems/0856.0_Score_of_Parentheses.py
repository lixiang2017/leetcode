'''
stack
T: O(N)
S: O(N)

Runtime: 32 ms, faster than 86.28% of Python3 online submissions for Score of Parentheses.
Memory Usage: 13.9 MB, less than 30.17% of Python3 online submissions for Score of Parentheses.
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    part_sum = 0
                    while stack and stack[-1] != '(':
                        part_sum += stack.pop()
                    stack.pop()
                    stack.append(2 * part_sum)
        
        return sum(stack)
