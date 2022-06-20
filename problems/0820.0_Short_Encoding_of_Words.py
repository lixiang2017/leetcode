'''
hash set

Runtime: 187 ms, faster than 78.14% of Python3 online submissions for Short Encoding of Words.
Memory Usage: 14.6 MB, less than 76.28% of Python3 online submissions for Short Encoding of Words.
'''
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        distinct = set(words)
        for word in words:
            for i in range(1, len(word)):
                distinct.discard(word[i: ])
        return sum(len(word) + 1 for word in distinct)


'''
trie

Runtime: 266 ms, faster than 52.09% of Python3 online submissions for Short Encoding of Words.
Memory Usage: 16.3 MB, less than 55.81% of Python3 online submissions for Short Encoding of Words.
'''
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        nodes = [reduce(dict.__getitem__, word[:: -1], trie) for word in words]
        return sum(len(word) + 1 for word, node in zip(words, nodes) if len(node) == 0)
                        

'''
Runtime: 256 ms, faster than 57.21% of Python3 online submissions for Short Encoding of Words.
Memory Usage: 16.4 MB, less than 48.84% of Python3 online submissions for Short Encoding of Words.
'''
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        trie = {}
        nodes = []
        for word in words:
            now = trie 
            for ch in word[:: -1]:
                if ch in now:
                    now = now[ch]
                else:
                    now[ch] = {}
                    now = now[ch]
            nodes.append(now)
        return sum(len(word) + 1 for word, node in zip(words, nodes) if len(node) == 0)


'''

Runtime: 184 ms, faster than 79.07% of Python3 online submissions for Short Encoding of Words.
Memory Usage: 16.1 MB, less than 59.53% of Python3 online submissions for Short Encoding of Words.
'''
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        trie = {}
        nodes = []
        for word in words:
            now = trie 
            for ch in reversed(word):
                if ch in now:
                    now = now[ch]
                else:
                    now[ch] = {}
                    now = now[ch]
            nodes.append(now)
        return sum(len(word) + 1 for word, node in zip(words, nodes) if len(node) == 0)

