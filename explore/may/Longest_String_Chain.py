'''
approach: Sort + Hash Table + DP
Time: O(NlogN + N * W * W), where N is the number of words and W is the length of a word.
Space: O(N * W)

You are here!
Your runtime beats 30.57 % of python3 submissions.
You are here!
Your memory usage beats 54.50 % of python3 submissions.
'''


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda word: len(word))
        chain = collections.Counter()
        max_len = 0
        
        for word in words:
            for j in range(len(word)):
                curr_w = word[: j] + word[j + 1: ]
                chain[word] = max(chain[word], chain[curr_w] + 1)
            max_len = max(max_len, chain[word])
        
        return max_len
