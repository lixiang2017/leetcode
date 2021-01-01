'''
wrong

Input: "a"
"aa"
Output: null
Expected: "a"
'''



class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for element in t:
            if element not in s:
                return element