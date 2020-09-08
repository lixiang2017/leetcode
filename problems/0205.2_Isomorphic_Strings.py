'''
Success
Details 
Runtime: 28 ms, faster than 73.73% of Python online submissions for Isomorphic Strings.
Memory Usage: 14.8 MB, less than 18.42% of Python online submissions for Isomorphic Strings.
'''
'''
Say we have 2 strings 'add' and 'egg':
for the result to be true, one letter in the first string must have an unique mapping to one letter in the other string.
'a'->'e' and 'd'->'g'
And the number of such mapping should be the SAME as the number of different letters in the 2 strings.
And that is all we need to check.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

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