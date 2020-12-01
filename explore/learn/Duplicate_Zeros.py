'''
You are here!
Your runtime beats 80.46 % of python submissions
'''


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        new_arr = []
        for i in range(size):
            new_arr.append(arr[i])
            if arr[i] == 0:
                new_arr.append(arr[i])
            if len(new_arr) >= size:
                arr[:] = new_arr[:size]
                break
