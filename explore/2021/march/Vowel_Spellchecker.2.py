'''
approach: HashMap (Hash Set + Hash Table)

Runtime: 176 ms, faster than 84.00% of Python online submissions for Vowel Spellchecker.
Memory Usage: 16.1 MB, less than 60.00% of Python online submissions for Vowel Spellchecker.
'''


class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c for c in word)
        
        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}
        
        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)
        
        def solve(query):
            if query in words_perfect:
                return query
            
            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]
            
            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""
        
        return map(solve, queries)
