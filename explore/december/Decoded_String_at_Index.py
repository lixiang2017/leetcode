'''
33 / 45 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
"y959q969u3hb22odq595"
222280369
'''

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        decoded = ''
        for ch in S:
            if ord('a') <= ord(ch) <= ord('z'):
                decoded += ch
            else:
                decoded = decoded * int(ch)
            if len(decoded) >= K:
                return decoded[K - 1]
                