'''
49 / 49 test cases passed.
	Status: Accepted
Runtime: 436 ms
Memory Usage: 12.8 MB
'''

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        def count(O, P, rowOffset, colOffset):
        	sum = 0
        	for i in xrange(rowOffset, len(O)):
        		for j in xrange(colOffset, len(P)):
        			sum += O[i][j] * P[i - rowOffset][j - colOffset]
        	return sum

        res = 0
        for i in xrange(len(A)):
        	for j in xrange(len(B)):
        		# res = max(res, count(A, B, i, j))   # wrong answer
        		res = max(res, max(count(A, B, i, j), count(B, A, i, j)))
        return res

        

if __name__ == '__main__':
	A = [[1,1,0],
	    [0,1,0],
	    [0,1,0]]
	B = [[0,0,0],
	    [0,1,1],
	    [0,0,1]]
	assert Solution().largestOverlap(A, B) == 3