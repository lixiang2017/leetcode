'''
Success
Details 
Runtime: 172 ms, faster than 80.53% of Python online submissions for Reverse String.
Memory Usage: 18.7 MB, less than 51.79% of Python online submissions for Reverse String.
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    assert Solution().reverseString(s) == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    assert Solution().reverseString(s) == ["h", "a", "n", "n", "a", "H"]      