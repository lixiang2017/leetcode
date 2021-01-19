'''
Time: O(N ^ 2)
Space: O(1)

You are here!
Your runtime beats 8.77 % of python submissions.
You are here!
Your memory usage beats 24.18 % of python submissions.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        size = len(s)
        for i in range(size):
            # for j in range(i, size + 1):
            j = i + len(longest)
            while j <= size:
                substr = s[i: j]
                if substr == substr[::-1] and len(substr) > len(longest):
                    longest = substr
                j += 1
                
        return longest
        
