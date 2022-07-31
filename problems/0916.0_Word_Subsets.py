'''
hash table

Runtime: 1240 ms, faster than 53.34% of Python3 online submissions for Word Subsets.
Memory Usage: 18.5 MB, less than 73.00% of Python3 online submissions for Word Subsets.
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = Counter()
        for word in words2:
            for ch, cnt in Counter(word).items():
                universal[ch] = max(universal[ch], cnt)
        
        def isUniversal(word):
            c = Counter(word)
            return all(cnt <= c[ch] for ch, cnt in universal.items())
        
        return list(filter(isUniversal, words1))   
        

'''
美服的filter可直接作为返回。 国服的不行

Runtime: 1681 ms, faster than 26.01% of Python3 online submissions for Word Subsets.
Memory Usage: 18.4 MB, less than 94.33% of Python3 online submissions for Word Subsets.
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = Counter()
        for word in words2:
            for ch, cnt in Counter(word).items():
                universal[ch] = max(universal[ch], cnt)
        
        def isUniversal(word):
            c = Counter(word)
            return all(cnt <= c[ch] for ch, cnt in universal.items())
        
        return filter(isUniversal, words1)
        