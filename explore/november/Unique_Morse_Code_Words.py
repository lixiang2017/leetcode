'''
You are here!
Your runtime beats 23.38 % of python submissions.
'''



class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = set()
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",\
                      ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",\
                      "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            trans = ''.join([morse_code[ord(ch) - ord('a')] for ch in word])
            transformations.add(trans)
        
        return len(transformations)
        