'''
approach: Stack + Pair
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 75.13 % of python3 submissions.
You are here!
Your memory usage beats 18.07 % of python3 submissions.
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []   # [letter, cnt]
        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])
                
            while stack and stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop(-1)
        
        return ''.join([letter * cnt for letter, cnt in stack])
        
'''
approach: Stack + Pair
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 33.78 % of python3 submissions.
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []   # [letter, cnt]
        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop(-1)
            else:
                stack.append([letter, 1])

        return ''.join([letter * cnt for letter, cnt in stack])
