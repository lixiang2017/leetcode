'''
hash table + sort

Runtime: 122 ms, faster than 37.74% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 13.8 MB, less than 99.56% of Python3 online submissions for Top K Frequent Words.
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        pairs = [(-cnt, word) for word, cnt in c.items()]
        pairs.sort()
        return [pairs[i][1] for i in range(k)]
