'''
Time: O(N), where N is the length of the given string.
Space: O(N), where N is the length of the given string.

Success
Details 
Runtime: 84 ms, faster than 23.78% of Python online submissions for ZigZag Conversion.
Memory Usage: 14 MB, less than 7.26% of Python online submissions for ZigZag Conversion.
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        
        rows = [[] for _ in range(numRows)]
        
        size = len(s)
        i = 0
        direction = 1  # 1 for down, -1 for up
        curRowIdx = 0
        while i < size:
            rows[curRowIdx].append(s[i])
            if curRowIdx == numRows - 1:
                direction = -1
            if curRowIdx == 0:
                direction = 1
                
            curRowIdx += direction
            
            i += 1
        
        return ''.join([''.join(row) for row in rows])

    
'''
"AB"
1
'''