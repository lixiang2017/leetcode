'''
Success
Details
Runtime: 20 ms, faster than 54.89% of Python online submissions for Occurrences After Bigram.
Memory Usage: 13.7 MB, less than 14.67% of Python online submissions for Occurrences After Bigram.
'''


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        thirds = []
        words = text.split()
        size = len(words)
        
        for i in xrange(size - 2):
            if words[i] == first and words[i + 1] == second:
                thirds.append(words[i + 2])
        return thirds
        