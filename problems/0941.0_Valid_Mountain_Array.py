'''
T: O(N)
S: O(1)

Runtime: 192 ms, faster than 95.90% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.6 MB, less than 61.89% of Python3 online submissions for Valid Mountain Array.
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, n = 0, len(arr)
        if n < 3:
            return False
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
        
