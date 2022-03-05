'''
simulation/iteration
T: O(query_row * query_row)
S: O(query_row)

Runtime: 168 ms, faster than 55.34% of Python3 online submissions for Champagne Tower.
Memory Usage: 13.9 MB, less than 81.55% of Python3 online submissions for Champagne Tower.
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        row: i-th (0-indexed),  cups_cnt: i + 1, streams count to next row: (i + 1) * 2
        next_row: i + 1, cups_cnt: i + 2, ...
        '''
        cur_cups = [poured]
        for row in range(query_row):
            # add two 0 cups
            cur_cups = [0] + cur_cups + [0]
            next_cups = [0] * (row + 2)
            for i in range(row + 2):
                # next_cups[i] = (cur_cups[i] + cur_cups[i + 1]) / 2   # wrong
                next_cups[i] = ( max(cur_cups[i] - 1, 0) + max(cur_cups[i + 1] -1, 0) ) / 2
            
            # update
            cur_cups = next_cups
        
        return min(1, cur_cups[query_glass])


'''
Runtime: 194 ms, faster than 42.72% of Python3 online submissions for Champagne Tower.
Memory Usage: 14 MB, less than 81.55% of Python3 online submissions for Champagne Tower.
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        row: i-th (0-indexed),  cups_cnt: i + 1, streams count to next row: (i + 1) * 2
        next_row: i + 1, cups_cnt: i + 2, ...
        '''
        cur_cups = [poured]
        for row in range(query_row):
            # add two 0 cups
            cur_cups = [0] + cur_cups + [0]
            next_cups = [0] * (row + 2)
            for i in range(row + 2):
                # next_cups[i] = (cur_cups[i] + cur_cups[i + 1]) / 2   # wrong
                next_cups[i] = ( max(cur_cups[i] - 1, 0) + max(cur_cups[i + 1] -1, 0) ) / 2
                
            if all(0 == c for c in next_cups):
                return 0
            
            # update
            cur_cups = next_cups
        
        return min(1, cur_cups[query_glass])
        