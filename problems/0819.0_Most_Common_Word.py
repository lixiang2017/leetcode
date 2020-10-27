'''

'''


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import string
        from collections import Counter
        
        paragraph = paragraph.lower()
        # words = paragraph.split()
        # words = [word if word[-1] in string.ascii_lowercase else word[: -1] for word in paragraph.split()]
        
        # replace punctuation symbols with space
        size = len(paragraph)
        for i in xrange(size):
            if paragraph[i] in "!?',;.":
                # paragraph[i] = ' '  # TypeError: 'unicode' object does not support item assignment"
                paragraph = paragraph[ : i] + ' ' + paragraph[i + 1 : ]
                
                
        words = paragraph.split()
        
        word_counter = Counter(words)
        word_counter = {word: count for word, count in word_counter.iteritems() if word not in banned}
        
        most_common, times = '', 0
        for word, count in word_counter.iteritems():
            if count > times:
                times = count
                most_common = word
        
        return most_common

    
    
'''
# not seperated by space !
Wrong Answer
Details 
Input
"a, a, a, a, b,b,b,c, c"
["a"]
Output
"b,b,b,c"
Expected
"b"
'''

'''
TypeError: 'unicode' object does not support item assignment
    paragraph[i] = ' '
Line 19 in mostCommonWord (Solution.py)
    ret = Solution().mostCommonWord(param_1, param_2)
Line 71 in _driver (Solution.py)
    _driver()
Line 81 in <module> (Solution.py)
'''


