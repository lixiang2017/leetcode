'''
You are here!
Your runtime beats 79.55 % of python submissions.
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
                size *= int(S[pos])
            else:
                size += 1
                if size == K:
                    return S[pos]
            if size >= K:
                break
                
        for ch in reversed(S[:pos + 1]):
            K %= size
            if K == 0 and ch.isalpha():
                return ch
            
            if ch.isdigit():
                size /= int(ch)
            else:
                size -= 1
        