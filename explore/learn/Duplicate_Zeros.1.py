'''
without using additional space

You are here!
Your runtime beats 36.17 % of python submissions.
'''

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        while i < size:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 2
            else:
                i += 1
                