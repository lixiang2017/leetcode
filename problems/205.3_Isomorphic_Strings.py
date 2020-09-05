'''
Success
Details 
Runtime: 40 ms, faster than 37.34% of Python online submissions for Isomorphic Strings.
Memory Usage: 12.6 MB, less than 71.05% of Python online submissions for Isomorphic Strings.
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(i) for i in s] == [t.find(j) for j in t]

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