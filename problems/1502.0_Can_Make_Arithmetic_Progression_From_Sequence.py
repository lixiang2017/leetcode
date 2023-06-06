'''
Runtime: 57 ms, faster than 32.76% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
Memory Usage: 16.5 MB, less than 20.83% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != d:
                return False
        return True
    
    