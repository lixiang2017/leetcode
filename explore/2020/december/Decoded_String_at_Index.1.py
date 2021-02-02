'''
approach #1: work backwards

You are here!
Your runtime beats 52.27 % of python submissions.
'''


class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        for ch in S:
            if ch.isalpha():
                size += 1
            else:
                size *= int(ch)
            
        for ch in reversed(S):
            K %= size
            
            if K == 0 and ch.isalpha():
                return ch
            
            if ch.isalpha():
                size -= 1
            else:   # ch.isdigit():
                size /= int(ch)
