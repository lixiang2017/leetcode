'''
approach: Hash Table

Success
Details 
Runtime: 12 ms, faster than 93.88% of Python online submissions for Keyboard Row.
Memory Usage: 13.4 MB, less than 90.31% of Python online submissions for Keyboard Row.
'''


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        one = "qwertyuiop"
        two = "asdfghjkl"
        three = "zxcvbnm"
        position = {}
        for letter in one:
            position[letter] = 1
        for letter in two:
            position[letter] = 2
        for letter in three:
            position[letter] = 3
        
        onlyOne = []
        for word in words:
            pos = set()
            for letter in word.lower():
                pos.add(position[letter])
            if len(pos) == 1:
                onlyOne.append(word)
        
        return onlyOne
    