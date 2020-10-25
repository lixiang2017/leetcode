'''
Success
Details 
Runtime: 68 ms, faster than 99.46% of Python online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 15.6 MB, less than 18.01% of Python online submissions for Find Smallest Letter Greater Than Target.
'''



class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        '''
        import string
        for ch in string.ascii_lowercase:
            if ord(ch) > ord(target) and ch in letters:
                return ch
        return letters[0]
        '''
    
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
            
        return letters[0]



'''
Success
Details 
Runtime: 80 ms, faster than 87.63% of Python online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 15.4 MB, less than 18.01% of Python online submissions for Find Smallest Letter Greater Than Target.
'''


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        seen = [letters[0]]
        for letter in letters:
            if seen[-1] != letter:
                seen.append(letter)
        for s in seen:
            if ord(s) > ord(target):
                return s
        return seen[0]
        