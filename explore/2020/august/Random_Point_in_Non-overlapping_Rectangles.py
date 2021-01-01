'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3433/

Q: How do localtest?

# Python3
Success
Details
Runtime: 384 ms, faster than 6.36% of Python3 online submissions for Random Point in Non-overlapping Rectangles.
Memory Usage: 17.5 MB, less than 72.83% of Python3 online submissions for Random Point in Non-overlapping Rectangles. 
'''

import random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.weights = []
        for [x_bl, y_bl, x_tr, y_tr] in self.rects:
        	self.weights.append((x_tr - x_bl + 1) * (y_tr - y_bl + 1))

        

    def pick(self):
        """
        :rtype: List[int]
        """
        [x_bl, y_bl, x_tr, y_tr] = random.choices(
        	self.rects, weights = self.weights
        	)[0]

        res = [
        	random.randrange(x_bl, x_tr + 1),
        	random.randrange(y_bl, y_tr + 1)
        ]
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

if __name__ == '__main__':
	subroutines = ["Solution","pick","pick","pick"]
	# rects = [[[[1,1,5,5]]],[],[],[]]
	rects = [[1,1,5,5]]
	# Output: [null,[4,1],[4,1],[3,3]]
	obj = Solution(rects)
	print(obj.pick())


	subroutines = ["Solution","pick","pick","pick","pick","pick"]
	# rects = [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
	rects = [[-2,-2,-1,-1],[1,0,3,0]]
	# Output: [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
	obj = Solution(rects)
	print(obj.pick())

