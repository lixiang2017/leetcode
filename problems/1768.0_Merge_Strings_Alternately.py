'''
Runtime: 35 ms, faster than 42.24% of Python3 online submissions for Merge Strings Alternately.
Memory Usage: 13.7 MB, less than 95.97% of Python3 online submissions for Merge Strings Alternately.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([a + b for a, b in zip_longest(word1, word2, fillvalue='')])
        

'''
Runtime: 39 ms, faster than 14.51% of Python3 online submissions for Merge Strings Alternately.
Memory Usage: 13.9 MB, less than 9.46% of Python3 online submissions for Merge Strings Alternately.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
        
        