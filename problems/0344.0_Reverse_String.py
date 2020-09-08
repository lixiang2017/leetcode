'''
Success
Details 
Runtime: 184 ms, faster than 34.82% of Python online submissions for Reverse String.
Memory Usage: 18.6 MB, less than 71.43% of Python online submissions for Reverse String.

# BUG
Runtime Error
's' must consist of values from -2147483648 to 2147483647 only
# issue
https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/13
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
