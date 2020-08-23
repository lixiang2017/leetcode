'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3433/
# python3
You are here!
Your runtime beats 34.68 % of python3 submissions.
'''

import random
import bisect

from itertools import accumulate

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        w = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.weights = [i / sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        """
        :rtype: List[int]
        """
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect]
        return [random.randint(x1, x2), random.randint(y1, y2)]



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

