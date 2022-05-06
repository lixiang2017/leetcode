'''
stack

Runtime: 212 ms, faster than 26.34% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
Memory Usage: 18.6 MB, less than 75.09% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # [char, count]
        stack = []
        for i, ch in enumerate(s):
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        
        return ''.join(ch * cnt for ch, cnt in stack)
            