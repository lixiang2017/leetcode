'''
You are here!
Your runtime beats 100.00 % of python submissions.
'''


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L, size = 10, len(s)
        seen, output = set(), set()
        
        for i in xrange(size - L + 1):
            subseq = s[i : i + L]
            if subseq in seen:
                output.add(subseq)
            seen.add(subseq)
        
        return output
        