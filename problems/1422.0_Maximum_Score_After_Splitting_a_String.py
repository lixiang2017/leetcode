'''
Success
Details
Runtime: 20 ms, faster than 87.13% of Python online submissions for Maximum Score After Splitting a String.
Memory Usage: 13.8 MB, less than 23.39% of Python online submissions for Maximum Score After Splitting a String.
'''


class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        zeros = [0 for i in xrange(size)]
        ones = [0 for i in xrange(size)]
        
        current_zeros = 0
        current_ones = 0
        for i in xrange(size):
            if s[i] == '0':
                current_zeros += 1
            else:
                current_ones += 1
            zeros[i] = current_zeros
            ones[i] = current_ones
        
        max_score = 0
        # for i in xrange(size):
        #  two non-empty substrings 
        for i in xrange(size - 1):
            score = zeros[i] + current_ones - ones[i]
            max_score = max(max_score, score)
        
        return max_score
            
        
'''
Wrong Answer
Details
Input
"00"
Output
2
Expected
1

splitting the string into two non-empty substrings 
'''