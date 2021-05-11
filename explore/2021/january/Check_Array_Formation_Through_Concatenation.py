'''
approach: brute force
Time: O(n^2)
Space: O(1)

You are here!
Your runtime beats 88.62 % of python submissions.
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
        size = len(arr)
        i = 0
        while i < size:
            found = False
            for piece in pieces:
                if piece[0] != arr[i]:
                    continue
                if piece[0] == arr[i]:
                    found = True
                    piece_len = len(piece)
                    if piece == arr[i : i + piece_len]:
                        i += piece_len
                        break
                    else:
                        return False
                    
            if not found:
                return False
            
        return True
    




'''
[85]
[[85]]
[15,88]
[[88],[15]]
[49,18,16]
[[16,18,49]]
[91,4,64,78]
[[78],[4,64],[91]]
[1,3,5,7]
[[2,4,6,8]]
'''