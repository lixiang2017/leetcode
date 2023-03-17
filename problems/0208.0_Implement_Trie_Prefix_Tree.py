'''
Runtime: 176 ms, faster than 75.18% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 33.4 MB, less than 14.24% of Python3 online submissions for Implement Trie (Prefix Tree).
'''
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Trie:

    def __init__(self):
        self.t = TrieNode()

    def insert(self, word: str) -> None:
        t = self.t
        for ch in word:
            t = t.children[ch]
        t.word = word

    def search(self, word: str) -> bool:
        t = self.t
        for ch in word:
            if ch not in t.children:
                return False
            t = t.children[ch]
        return t.word == word

    def startsWith(self, prefix: str) -> bool:
        t = self.t
        for ch in prefix:
            if ch not in t.children:
                return False
            t = t.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''
Runtime: 121 ms, faster than 96.87% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.6 MB, less than 88.96% of Python3 online submissions for Implement Trie (Prefix Tree).
'''
class Trie:

    def __init__(self):
        self.t = {}

    def insert(self, word: str) -> None:
        t = self.t
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t['#'] = True

    def search(self, word: str) -> bool:
        t = self.t
        for ch in word:
            if ch not in t:
                return False
            t = t[ch]
        return '#' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.t
        for ch in prefix:
            if ch not in t:
                return False
            t = t[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''
Runtime: 150 ms, faster than 87.58% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 28 MB, less than 82.02% of Python3 online submissions for Implement Trie (Prefix Tree).
'''
T = lambda : defaultdict(T)

class Trie:

    def __init__(self):
        self.t = T()

    def insert(self, word: str) -> None:
        t = self.t
        for ch in word:
            t = t[ch]
        t['#'] = True

    def search(self, word: str) -> bool:
        t = self.t
        for ch in word:
            if ch not in t:
                return False
            t = t[ch]
        return '#' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.t
        for ch in prefix:
            if ch not in t:
                return False
            t = t[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



