'''
approach : recursive

You are here!
Your runtime beats 90.91 % of python submissions.
'''

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        length = len(S)
        pos = 0
        for pos in range(length):
            if S[pos].isdigit():
                if size * int(S[pos]) >= K:
                    return self.decodeAtIndex(S[:pos], (K - 1) % size + 1)
                size *= int(S[pos])
            else:
                size += 1
                if size == K:
                    return S[pos]
                    