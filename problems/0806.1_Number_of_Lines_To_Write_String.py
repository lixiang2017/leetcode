'''
Success
Details 
Runtime: 12 ms, faster than 98.75% of Python online submissions for Number of Lines To Write String.
Memory Usage: 13.5 MB, less than 26.25% of Python online submissions for Number of Lines To Write String.
'''


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """        
        lines, last_width = 1, 0
        for ch in S:
            width = widths[ord(ch) - ord('a')]
            last_width += width
            if last_width > 100:
                lines += 1
                last_width = width
                
        return [lines, last_width]
            