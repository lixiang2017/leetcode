'''
Approach 2: Character Processing in One-Pass

Success
Details 
Runtime: 28 ms, faster than 58.68% of Python online submissions for Most Common Word.
Memory Usage: 13.7 MB, less than 36.09% of Python online submissions for Most Common Word.
'''

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []
        
        for p, char in enumerate(paragraph):  # p for position
            #1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph) - 1:
                    continue
            
            #2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = ''.join(word_buffer)
                if word not in banned_words:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                    
                # reset the buffer for the next word
                word_buffer = []
                    
        return ans
        