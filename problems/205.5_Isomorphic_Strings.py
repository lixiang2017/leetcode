'''
Success
Details 
Runtime: 168 ms, faster than 15.08% of Python online submissions for Isomorphic Strings.
Memory Usage: 14.5 MB, less than 44.74% of Python online submissions for Isomorphic Strings.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())

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