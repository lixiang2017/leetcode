'''
use dict
Time: O(N)
Space: O(N) to store dict

You are here!
Your runtime beats 66.31 % of python submissions.
You are here!
Your memory usage beats 20.18 % of python submissions.
'''



class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        self = {piece[0]: piece for piece in pieces}
        concatenation = []
        
        for num in arr:
            concatenation += self.get(num, [])
        
        return concatenation == arr
        