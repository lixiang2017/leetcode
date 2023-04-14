'''
stack
T: O(2N)
S: O(N)

Runtime: 162 ms, faster than 7.39% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14.2 MB, less than 63.80% of Python3 online submissions for Validate Stack Sequences.
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack, i = [], 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return stack == []
        
'''
Runtime: 74 ms, faster than 55.80% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 14 MB, less than 85.31% of Python3 online submissions for Validate Stack Sequences.
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, n = 0, len(pushed)
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
        