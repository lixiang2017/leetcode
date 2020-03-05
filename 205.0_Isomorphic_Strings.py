'''
Wrong Answer
!!! while preserving the order of characters. 
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # len
        if len(s) != len(t):
            return False
        
        # hash map, for every character
        # A ... Z ... a ... z
        list_s = [0] * ord('z') + [0]
        list_t = [0] * ord('z') + [0]
        for c in s:
            list_s[ord(c)] += 1
        for c in t:
            list_t[ord(c)] += 1
        
        # print s, t
        # print 's: ', sorted(list_s)
        # print 't: ', sorted(list_t)
        return sorted(list_s) == sorted(list_t)

if __name__ == "__main__":
    s = "egg"
    t = "add"
    assert Solution().isIsomorphic(s, t)

    s = "foo"
    t = "bar"
    assert not Solution().isIsomorphic(s, t)

    s = "paper"
    t = "title"
    assert Solution().isIsomorphic(s, t)

    # Expected false
    s = "aba"
    t = "baa"
    assert not Solution().isIsomorphic(s, t)