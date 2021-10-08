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
