'''
Runtime: 752 ms, faster than 61.08% of Python3 online submissions for Stream of Characters.
Memory Usage: 42.9 MB, less than 16.17% of Python3 online submissions for Stream of Characters.
'''
class Trie:
    def __init__(self):
        self.t = defaultdict(Trie)
        self.t['isWord'] = False
    
    def add(self, word):
        node = self
        n = len(word)
        for ch in word:
            node = node.t[ch]
        node.t['isWord'] = True
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[:: -1])
        # history query list
        self.q = []

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        n = len(self.q)
        node = self.trie
        for i in range(n - 1, -1, -1):
            ch = self.q[i]
            if ch in node.t:
                node = node.t[ch]
                if node.t['isWord']:
                    return True
            else:
                return False
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


'''
Runtime: 716 ms, faster than 66.02% of Python3 online submissions for Stream of Characters.
Memory Usage: 43 MB, less than 14.07% of Python3 online submissions for Stream of Characters.
'''
class Trie:
    def __init__(self):
        self.t = defaultdict(Trie)
        self.isWord = False
    
    def add(self, word):
        node = self
        n = len(word)
        for ch in word:
            node = node.t[ch]
        node.isWord = True
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[:: -1])
        # history query list
        self.q = []

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        n = len(self.q)
        node = self.trie
        for i in range(n - 1, -1, -1):
            ch = self.q[i]
            if ch in node.t:
                node = node.t[ch]
                if node.isWord:
                    return True
            else:
                return False
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)




'''
Runtime: 1080 ms, faster than 35.18% of Python3 online submissions for Stream of Characters.
Memory Usage: 46.5 MB, less than 5.39% of Python3 online submissions for Stream of Characters.
'''
class Trie(dict):
    def __init__(self):
        self = defaultdict(Trie)
        self['isWord'] = False

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            self.__dict__[key] = Trie()
            return self.__dict__[key]

    def __contains__(self, item):
        return item in self.__dict__
 
    def add(self, word):
        node = self
        n = len(word)
        for ch in word:
            node = node[ch]
        node['isWord'] = True
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[:: -1])
        # history query list
        self.q = []

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        n = len(self.q)
        node = self.trie
        for i in range(n - 1, -1, -1):
            ch = self.q[i]
            if ch in node:
                node = node[ch]
                if node['isWord']:
                    return True
            else:
                return False
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


