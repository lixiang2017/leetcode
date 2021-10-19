'''
Stack / Monotonic Stack
降序的stack

T: O(2N)
S: O(2N)

Runtime: 224 ms, faster than 65.52% of Python3 online submissions for Next Greater Element II.
Memory Usage: 16.5 MB, less than 9.64% of Python3 online submissions for Next Greater Element II.
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack, greater = [], [-1] * N 
        for i, x in enumerate(nums + nums):
            while stack and stack[-1][0] < x:
                top, idx = stack.pop()
                if idx < N:
                    greater[idx] = x
            stack.append([x, i])
        return greater

'''
Input
[100,1,11,1,120,111,123,1,-1,-100]
Output
[120,120,120,120,123,123,-1,120,100,100]
Expected
[120,11,120,120,123,123,-1,100,100,100]
'''
