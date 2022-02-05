'''
Runtime: 1381 ms, faster than 20.22% of Python3 online submissions for Contiguous Array.
Memory Usage: 19.3 MB, less than 24.67% of Python3 online submissions for Contiguous Array.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pos = {0: -1}
        maxlen = count = 0
        for i, x in enumerate(nums):
            if x == 1:
                count += 1
            else:
                count -= 1
            if count in pos:
                maxlen = max(maxlen, i - pos[count])
            else:
                pos[count] = i
        
        return maxlen
        
        
        