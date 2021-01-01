'''
You are here!
Your runtime beats 8.00 % of python submissions.
'''


class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        how_full = []
        
        # row -> cups
        # the number of cups in one row is (row i-th) + 1
        for row in range(query_row + 1):
            row_how_full = []
            cups = row + 1
            if row == 0:
                row_how_full = [poured]
                how_full.append(row_how_full)
                continue
            
            last_row = how_full[-1]    # how_full[row - 1]
            for cup in range(cups):
                new_last_row = [0] + last_row + [0]
                shoulders = (new_last_row[cup] - 1 if new_last_row[cup] > 1 else 0) +  (new_last_row[cup + 1] - 1 if new_last_row[cup + 1] > 1 else 0) 
                row_how_full.append(shoulders / 2.0)
            how_full.append(row_how_full)
            
        
        return 1 if how_full[query_row][query_glass] >= 1 else how_full[query_row][query_glass]
        
        