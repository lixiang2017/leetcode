'''
Success
Details 
Runtime: 20 ms, faster than 83.73% of Python online submissions for Unique Morse Code Words.
Memory Usage: 13.6 MB, less than 26.42% of Python online submissions for Unique Morse Code Words.
'''


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        import string
        letter2morse = {letter: morse for letter, morse in  zip(string.ascii_lowercase, morses)}
        
        transformations = set()
        for word in words:
            trans = ''.join([letter2morse[letter] for letter in word])
            transformations.add(trans)
        
        return len(transformations)