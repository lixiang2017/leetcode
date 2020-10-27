'''
Success
Details 
Runtime: 20 ms, faster than 75.00% of Python online submissions for Number of Lines To Write String.
Memory Usage: 13.5 MB, less than 26.25% of Python online submissions for Number of Lines To Write String.
'''


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 0
        last_width = 0
        import string
        letter2width = {letter: width for letter, width in zip(string.ascii_lowercase, widths)}
        
        for letter in S:
            if letter2width[letter] + last_width > 100:
                lines += 1
                last_width = letter2width[letter]
            else:
                last_width += letter2width[letter]
        
        return [lines + 1, last_width]