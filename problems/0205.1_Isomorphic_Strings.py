'''
Success
Details 
Runtime: 40 ms, faster than 37.34% of Python online submissions for Isomorphic Strings.
Memory Usage: 13 MB, less than 52.63% of Python online submissions for Isomorphic Strings.
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
        
        size = len(s)
        m1, m2 = [0] * 256, [0]* 256

        for i in range(0, size):
            if m1[ord(s[i])] != m2[ord(t[i])]: return False
            m1[ord(s[i])] = i + 1       # ASCII -> index
            m2[ord(t[i])] = i + 1       # ASCII -> index
        return True


'''
if m1[ord(s[i])] != m2[ord(t[i])] 
will check whether the char has appeared before
'''

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