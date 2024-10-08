'''
follow-up: infinite board

You are here!
Your runtime beats 91.56 % of python submissions.
You are here!
Your memory usage beats 75.52 % of python submissions.

ref:
https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution/201780
https://leetcode.com/problems/game-of-life/solution/
https://www.youtube.com/watch?v=E65KQ_jwROo
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        live = [(i, j) for i, row in enumerate(board)
                        for j, live in enumerate(row) if live]
        live = self.gameOfLifeInfinite(live)
        
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                row[j] = int((i, j) in live)
        
    
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J) for (i, j) in live
                                        for I in range(i - 1, i + 2)
                                        for J in range(j - 1, j + 2)
                                        if I != i or J != j)
        
        #return {ij for ij in ctr
        #            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}  #ok  # set
        return [ij for ij in ctr
                    if ctr[ij] == 3 or ctr[ij] == 2 and ij in live]    # also work  # list
    