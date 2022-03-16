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
        
