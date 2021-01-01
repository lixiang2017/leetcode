'''
You are here!
Your runtime beats 89.00 % of python submissions.
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashmap = {}
        size = len(s)
        for i in xrange(0, size - 9):
            subseq = s[i: i + 10]
            if subseq in hashmap:
                hashmap[subseq] += 1
            else:
                hashmap[subseq] = 1
        
        # print 'hashmap: ', hashmap
        repeatition = []
        for subseq, count in hashmap.iteritems():
            if count > 1:
                repeatition.append(subseq)
        return repeatition
        