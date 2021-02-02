'''
You are here!
Your runtime beats 77.45 % of python submissions.
'''


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        size = len(arr)
        if size < 3: return False
        i = 1
        while i < size - 1:
            if arr[i] > arr[i - 1]:
                i += 1
                continue
            else:
                break
        if i == 1: return False  # [9,8,7,6,5,4,3,2,1,0]  !!!
        while i < size:
            if arr[i] < arr[i - 1]:
                i += 1
                continue
            else:
                break
        
        return True if i == size else False

'''
Input: [9,8,7,6,5,4,3,2,1,0]
Output: true
Expected: false
'''
