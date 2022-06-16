'''
hash table

Runtime: 153 ms, faster than 88.34% of Python3 online submissions for Longest String Chain.
Memory Usage: 14.4 MB, less than 48.74% of Python3 online submissions for Longest String Chain.
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        len2words = defaultdict(set)
        word2ans = defaultdict(int)
        ans = 0
        for w in words:
            word2ans[w] = 1
            len2words[len(w)].add(w)
        
        for l in range(16, 0, -1):
            for w in len2words[l]:
                ans = max(ans, word2ans[w])
                # try to remove each letter
                for j in range(l):
                    nw = w[: j] + w[j + 1: ]
                    if nw in len2words[l - 1]:
                        word2ans[nw] = max(word2ans[nw], word2ans[w] + 1)
                        ans = max(ans, word2ans[nw])
        return ans