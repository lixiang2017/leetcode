'''
Approach 1: String Processing in Pipeline

Success
Details 
Runtime: 20 ms, faster than 93.09% of Python online submissions for Most Common Word.
Memory Usage: 13.8 MB, less than 34.86% of Python online submissions for Most Common Word.
'''

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        #2). split the string into words
        words = normalized_str.split()
        
        word_count = defaultdict(int)
        banned_words = set(banned)
        
        #3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1
        
        #4). return the word with highest frequency
        print max(word_count.items(), key=operator.itemgetter(1))  # (u'ball', 2)
        return max(word_count.items(), key=operator.itemgetter(1))[0]
        