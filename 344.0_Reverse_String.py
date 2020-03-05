'''
Runtime Error
's' must consist of values from -2147483648 to 2147483647 only
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in xrange(l / 2):
            s[i], s[l - i - 1] = s[l - i - 1], s[i]

        # for test, no use
        print s
        return s

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    assert Solution().reverseString(s) == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    assert Solution().reverseString(s) == ["h", "a", "n", "n", "a", "H"]      