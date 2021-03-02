'''
You are here!
Your runtime beats 32.16 % of python submissions.

You are here!
Your runtime beats 90.85 % of python submissions.
'''



class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # return sorted([a * a for a in A])
        negative_squares = [x * x for x in A if x < 0][::-1]
        positive_squares = [x * x for x in A if x >= 0]
        
        sorted_squares = []
        negative_size = len(negative_squares)
        positive_size = len(A) - negative_size
        i, j = 0, 0
        while i < negative_size and j < positive_size:
            neg = negative_squares[i]
            pos = positive_squares[j]
            if neg < pos:
                sorted_squares.append(neg)
                i += 1
            else:
                sorted_squares.append(pos)
                j += 1
        
        if i == negative_size:
            sorted_squares += positive_squares[j:]
        
        if j == positive_size:
            sorted_squares += negative_squares[i:]
        
        return sorted_squares
    