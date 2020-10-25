'''
Success
Details 
Runtime: 76 ms, faster than 94.62% of Python online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 15.3 MB, less than 18.01% of Python online submissions for Find Smallest Letter Greater Than Target.
'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        import string
        for ch in string.ascii_lowercase:
            if ord(ch) > ord(target) and ch in letters:
                return ch
        
        return letters[0]