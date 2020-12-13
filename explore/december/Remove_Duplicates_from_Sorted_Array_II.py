'''
Approach: Two Pointers

You are here!
Your runtime beats 65.86 % of python submissions.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        size = len(nums)
        i = j = 1
        meetTwo = False
        pre = nums[0]
        while i < size and j < size:
            while meetTwo and j < size and pre == nums[j]:
                j += 1
                continue
            if j == size: break
                
            nums[i] = nums[j]

            if pre == nums[i]:
                meetTwo = True
            else:
                meetTwo = False
                pre = nums[i]
            i += 1
            j += 1
            continue
                    
        return i
    
'''
[1,1,1]
'''
