'''
Time: O(N^2)
Space: O(N)

You are here!
Your runtime beats 7.74 % of python submissions.
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
        concatenation = []
        
        for i in range(len(arr)):
            for piece in pieces:
                if piece == arr[i : i + len(piece)]:
                    concatenation.extend(piece)
        
        out = (arr == concatenation)
        return out